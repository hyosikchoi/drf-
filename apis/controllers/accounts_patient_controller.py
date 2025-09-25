from domains.accounts.models import Patient
from domains.accounts.service.accounts_patient_service import AccountsPatientService
from domains.commons.base_controller import BaseController


class AccountsPatientController(BaseController):
    class Meta:
        model = Patient

    service_class = AccountsPatientService
        