from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class AccountsPatientResSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(help_text=_("생성 일자"))
    updated_at = serializers.DateTimeField(help_text=_("수정 일자"))
    patient_uuid = serializers.UUIDField(help_text=_("환자 고유 번호"))
    description = serializers.CharField(help_text=_("환자 설명"))
    user_id = serializers.IntegerField(allow_null=True, help_text=_("의사 아이디"))
    is_deleted = serializers.BooleanField(default=False, help_text=_("삭제 여부"))
