from typing import TYPE_CHECKING, Optional

from django.db import models

from domains.accounts.service.accounts_organization_service import AccountsOrganizationService
from domains.commons.BaseController import BaseController
from domains.accounts.models.accounts_organization_model import Organization


class AccountsOrganizationController(BaseController):
    class Meta:
        model = Organization

    service_class: AccountsOrganizationService = AccountsOrganizationService



