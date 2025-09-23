from functools import wraps
from typing import Optional

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet


def normalize(
    req_serializer_class: type[Serializer] = None,
    res_serializer_class: type[Serializer] = None,
    many: bool = False,
    page: bool = False,
    partial: bool = False, # partial=True: 일부 필드만 제공해도 유효성 검사를 통과 (PATCH 요청에서 주로 사용), partial=False: 모든 required 필드가 제공되어야 유효성 검사 통과 (POST/PUT 요청에서 주로 사용)
):
    if page:
        many = True

    def request_wrapper(func):
        @wraps(func)
        def wrapper(view: GenericViewSet, request: Request, *args, **kwargs) -> Response:
            validated_data = _get_validated_data(request)
            result = func(view, validated_data, request, *args, **kwargs)

            if page:
                return _get_paginated_response(view, result)
            return _get_response(view, result)

        def _get_validated_data(request: Request) -> dict:
            validated_data = {}
            if req_serializer_class:
                data = request.data if request.method in ('PUT', 'POST', 'PATCH') else request.query_params
                req_serializer = req_serializer_class(data = data, partial=partial)
                req_serializer.is_valid(raise_exception=True)
                validated_data = req_serializer.validated_data
            return validated_data

        def _get_paginated_response(view: GenericViewSet, result: Optional[QuerySet]) -> Response:
            paginated_queryset = view.paginate_queryset(queryset=result)
            if paginated_queryset is not None:
                return view.get_paginated_response(
                    res_serializer_class(paginated_queryset, many=many).data
                )
            return _get_response(result)

        def _get_response(result: Optional[QuerySet]) -> Response:
            if result is not None and isinstance(result, Response):
                return result
            if res_serializer_class:
                return Response(res_serializer_class(result, many=many, status= status.HTTP_200_OK).data)
            return Response(result, status=status.HTTP_200_OK)
        return wrapper
    return request_wrapper