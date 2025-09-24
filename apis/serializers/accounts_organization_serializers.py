from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class AccountsOrganizationResSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(help_text=_("생성 일자"))
    updated_at = serializers.DateTimeField(help_text=_("수정 일자"))
    name = serializers.CharField(help_text=_("이름"))
    organization_number = serializers.CharField(help_text=_("기관 번호"))
    address = serializers.CharField(help_text=_("기관 주소"))
    telephone_number = serializers.CharField(help_text=_("기관 전화번호"))


class AccountsOrganizationReqSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text=_("이름"))
    organization_number = serializers.CharField(required=False, help_text=_("기관 번호"), allow_null=True)
    address = serializers.CharField(required=False, help_text=_("기관 주소"), allow_null=True)
    telephone_number = serializers.CharField(required=False, help_text=_("기관 전화번호"), allow_null=True)
