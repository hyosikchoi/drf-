from typing import TYPE_CHECKING

from docutils.nodes import organization
from rest_framework.response import Response

from apis.controllers.accounts_organization_controller import AccountsOrganizationController
from domains.commons.BaseViewSet import BaseViewSet
from domains.accounts.models.accounts_organization_model import Organization
from rest_framework.request import Request

class AccountsOrganizationViewSet(BaseViewSet):
    serializer_class = None
    controller_class = AccountsOrganizationController
    queryset = Organization.objects

    def list(self, request: Request, *args, **kwargs) -> Response:
        organizations = self.controller_class().get_all()
        data = []
        for organization in organizations:
            data.append({
                'id': organization.id,
                'created_at': organization.created_at,
                'updated_at': organization.updated_at,
                'name': organization.name,
                'organization_number': organization.organization_number,
                'address': organization.address,
                'telephone_number': organization.telephone_number
            })
        return Response(data)
