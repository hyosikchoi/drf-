from domains.accounts.models.accounts_organization_model import Organization
from domains.accounts.service.accounts_organization_service import AccountsOrganizationService
from domains.commons.base_controller import BaseController


class AccountsOrganizationController(BaseController):
    class Meta:
        model = Organization

    service_class: AccountsOrganizationService = AccountsOrganizationService
