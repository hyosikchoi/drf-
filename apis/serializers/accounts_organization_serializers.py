from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class AccountsOrganizationResSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(help_text=_("생성 일자"))
    updated_at = serializers.DateTimeField(help_text=_("수정 일자"))
    name = serializers.CharField(help_text=_("이름"))
    organization_number = serializers.CharField(help_text=_("기관 번호"))
    address = serializers.CharField(help_text=_("기관 주소"))
    telephone_number = serializers.CharField(help_text=_("기관 전화번호"))