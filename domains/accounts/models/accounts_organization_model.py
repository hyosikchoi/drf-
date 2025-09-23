from django.db import models
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    class Meta:
        ordering = ["id"]
        db_table_comment = "기관"
        verbose_name = _("기관")


    created_at = models.DateTimeField(
        auto_now_add=True, # auto_now_add: 한 번만 설정 (불변), auto_now: 매번 갱신 (가변)
        null=True,
        blank=True,
        help_text=_("생성 일자"),
        db_comment="생성 일자"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        help_text=_("수정 일자"),
        db_comment="수정 일자"
    )

    name = models.TextField(
        null=True,
        blank=True,
        help_text=_("이름"),
        db_comment="이름"
    )

    organization_number = models.TextField(
        null=True,
        blank=True,
        help_text=_("기관 번호"),
        db_comment="기관 번호"
    )

    address = models.TextField(
        null=True,
        blank=True,
        help_text=_("기관 주소"),
        db_comment="기관 주소"
    )

    telephone_number = models.TextField(
        null=True,
        blank=True,
        help_text=_("기관 전화번호"),
        db_comment="기관 전화번호"
    )