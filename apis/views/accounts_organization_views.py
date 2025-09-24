from typing import TYPE_CHECKING

from rest_framework.response import Response

from apis.controllers.accounts_organization_controller import AccountsOrganizationController
from apis.serializers.accounts_organization_serializers import AccountsOrganizationResSerializer
from domains.commons.BaseViewSet import BaseViewSet
from domains.accounts.models.accounts_organization_model import Organization
from rest_framework.request import Request
from util.util_decorator import normalize_view

class AccountsOrganizationViewSet(BaseViewSet):
    serializer_class = AccountsOrganizationResSerializer
    controller_class = AccountsOrganizationController
    queryset = Organization.objects

    @normalize_view(req_serializer_class= None, res_serializer_class=AccountsOrganizationResSerializer, many=True)
    def list(self, request: Request, *args, **kwargs) -> Response:
        return self.controller_class().get_all()

