from typing import TYPE_CHECKING, Optional

from docutils.nodes import organization

from domains.accounts.models import Organization
from domains.commons.BaseService import BaseService


class AccountsOrganizationService(BaseService):
    class Meta:
        model = Organization


    def get_organization_list(self) -> list[Organization]:
        organizations = self.get_all().all()
        return list(organizations)

    def get_organization(self, organization_id: int) -> Optional[Organization]:
        return self.get(pk=organization_id)