from typing import TYPE_CHECKING, Optional

from docutils.nodes import organization

from domains.accounts.models import Organization
from domains.commons.BaseService import BaseService


class AccountsOrganizationService(BaseService):
    class Meta:
        model = Organization
