from rest_framework.request import Request
from rest_framework.response import Response

from apis.controllers.accounts_organization_controller import AccountsOrganizationController
from apis.serializers.accounts_organization_serializers import (
    AccountsOrganizationReqSerializer,
    AccountsOrganizationResSerializer,
)
from domains.accounts.models.accounts_organization_model import Organization
from domains.commons.base_view_set import BaseViewSet
from util.util_decorator import normalize_view


class AccountsOrganizationViewSet(BaseViewSet):
    serializer_class = AccountsOrganizationResSerializer
    controller_class = AccountsOrganizationController
    queryset = Organization.objects

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsOrganizationResSerializer, many=True)
    def list(self, validated_data: dict, request: Request, *args, **kwargs) -> Response:
        return self.controller_class().get_all()

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsOrganizationResSerializer)
    def retrieve(self, validated_data: dict, request: Request, pk: int, *args, **kwargs) -> Response:
        return self.controller_class().get(pk=pk)

    @normalize_view(
        req_serializer_class=AccountsOrganizationReqSerializer, res_serializer_class=AccountsOrganizationResSerializer
    )
    def create(self, validated_data: dict, request: Request, *args, **kwargs) -> Response:
        return self.controller_class().create(validated_data)

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsOrganizationResSerializer)
    def update(self, validated_data: dict, request: Request, pk: int, *args, **kwargs) -> Response:
        return self.controller_class().update(pk, request.data)
