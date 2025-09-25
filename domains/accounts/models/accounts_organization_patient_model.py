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
        unique_together = [['organization', 'patient']]  # 중복 관계 방지

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
        help_text=_("생성 일자"),
        db_comment="생성 일자",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text=_("수정 일자"),
        db_comment="수정 일자"
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        help_text=_("기관"),
        db_comment="기관 ID"
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        help_text=_("환자"),
        db_comment="환자 ID"
    )