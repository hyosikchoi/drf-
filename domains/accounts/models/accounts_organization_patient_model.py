from django.db import models
from django.utils.translation import gettext_lazy as _

from .accounts_organization_model import Organization
from .accounts_patient_model import Patient


class OrganizationPatient(models.Model):
    class Meta:
        ordering = ["id"]
        db_table = "accounts_organizationpatient"
        db_table_comment = "기관-환자 관계"
        verbose_name = _("기관-환자")
        unique_together = [["organization", "patient"]]  # 중복 관계 방지

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, help_text=_("기관"), db_comment="기관 ID")

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, help_text=_("환자"), db_comment="환자 ID")

    chart_number = models.TextField(help_text=_("차트 번호"), db_comment="차트 번호")

    # TODO 추후 accounts_user 테이블 생성후 외래키로 변경해야함.
    user_id = models.BigIntegerField(help_text=_("의사"), db_comment=_("의사"))
