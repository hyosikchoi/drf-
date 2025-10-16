from domains.accounts.models import OrganizationPatient
from domains.commons.base_service import BaseService


class AccountsOrganizationPatientService(BaseService):
    class Meta:
        model = OrganizationPatient

    def create_organization_and_patient_mapping(self, *args, **kwargs) -> OrganizationPatient:
        data = {
            "chart_number": kwargs.get("chart_number"),
            "patient_id": kwargs.get("patient_id"),
            "organization_id": 1,  # TODO user 의 기관 id 를 가져오긴 해야함.
            "user_id": 1,  # TODO user id 를 가져오긴 해야함.
        }
        row = self.Meta.model(**data)
        row.save()
        return row
