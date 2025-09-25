from django.db import models
from django.utils.translation import gettext_lazy as _


class Patient(models.Model):
    class Meta:
        ordering = ["id"]
        db_table_comment = "환자"
        verbose_name = _("환자")

    created_at = models.DateTimeField(auto_now_add=True, help_text=_("생성 일자"), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, help_text=_("수정 일자"), blank=True, null=True)
    patient_uuid = models.UUIDField(null=False, blank=False, help_text=_("환자 uuid"))
    description = models.TextField(help_text=_("환자 설명"))
    user_id = models.BigIntegerField(null=True, blank=True, help_text=_("의사 아이디"))
    is_deleted = models.BooleanField(default=False, help_text=_("삭제 여부"))
