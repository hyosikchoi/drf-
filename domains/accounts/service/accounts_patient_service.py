from domains.accounts.models import Patient
from domains.commons.base_service import BaseService


class AccountsPatientService(BaseService):
    class Meta:
        model = Patient
