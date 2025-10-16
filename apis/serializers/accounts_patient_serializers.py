from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from domains.accounts.models import Patient


class AccountsPatientReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["description", "chart_number"]

    chart_number = serializers.CharField(help_text=_("차트 번호"))


class AccountsPatientResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["patient_uuid"]
