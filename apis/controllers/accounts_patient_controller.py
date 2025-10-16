from django.db.models import QuerySet

from domains.accounts.models import Patient
from domains.accounts.service.accounts_patient_service import AccountsPatientService
from domains.commons.base_controller import BaseController


class AccountsPatientController(BaseController):
    class Meta:
        model = Patient

    service_class = AccountsPatientService

    def create_patient(self, validated_data: dict, *args, **kwargs) -> QuerySet:
        return self.service_class().create_patient(validated_data, *args, **kwargs)
        