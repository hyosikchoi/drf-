from django.db import models
from django.db.models import QuerySet

from domains.commons.base_service import BaseService


class BaseController:
    class Meta:
        model: type[models.Model] = None

    service_class: type[BaseService] = None

    def get_all(self, *args, **kwargs) -> QuerySet[models.Model]:
        return self.service_class().get_all(*args, **kwargs)

    def get(self, pk: int, *args, **kwargs) -> models.Model | None:
        return self.service_class().get(pk, *args, **kwargs)

    def create(self, validated_data: dict) -> models.Model:
        return self.service_class().create(validated_data)
