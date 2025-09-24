from domains.accounts.models import Organization
from domains.commons.base_service import BaseService


class AccountsOrganizationService(BaseService):
    class Meta:
        model = Organization
