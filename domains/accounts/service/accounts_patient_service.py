from rest_framework.exceptions import ValidationError

from domains.accounts.models import Patient
from domains.accounts.service.accounts_organization_patient_service import AccountsOrganizationPatientService
from domains.commons.base_service import BaseService


class AccountsPatientService(BaseService):
    class Meta:
        model = Patient

    def create_patient(self, validated_data: dict, *args, **kwargs) -> Patient | None:
        try:
            data = validated_data.copy()
            chart_number = data.pop("chart_number")
            row = self.Meta.model(**data)
            row.save()
            AccountsOrganizationPatientService().create_organization_and_patient_mapping(
                chart_number=chart_number, patient_id=row.pk
            )
            return row

        except ValidationError as e:
            raise e
