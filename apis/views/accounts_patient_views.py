from rest_framework.request import Request
from rest_framework.response import Response

from apis.controllers.accounts_patient_controller import AccountsPatientController
from apis.serializers.accounts_patient_serializers import AccountsPatientResSerializer
from domains.accounts.models import Patient
from domains.commons.base_view_set import BaseViewSet
from util.util_decorator import normalize_view


class AccountsPatientViewSet(BaseViewSet):
    serializer_class = AccountsPatientResSerializer
    controller_class = AccountsPatientController
    queryset = Patient.objects

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsPatientResSerializer, many=True)
    def list(self, validated_data: dict, request: Request, *args, **kwargs) -> Response:
        return self.controller_class().get_all()

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsPatientResSerializer)
    def retrieve(self, validated_data: dict, request: Request, pk: int, *args, **kwargs) -> Response:
        return self.controller_class().get(pk=pk)

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsPatientResSerializer)
    def create(self, validated_data: dict, request: Request, *args, **kwargs) -> Response:
        return self.controller_class().create(validated_data)

    @normalize_view(req_serializer_class=None, res_serializer_class=AccountsPatientResSerializer)
    def update(self, validated_data: dict, request: Request, pk: int, *args, **kwargs) -> Response:
        return self.controller_class().update(pk, request.data)

    @normalize_view(req_serializer_class=None, res_serializer_class=None)
    def destroy(self, validated_data: dict, request: Request, pk: int, *args, **kwargs) -> str:
        self.controller_class().delete(pk)
        return "SUCCESS"
