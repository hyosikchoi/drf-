from typing import TYPE_CHECKING, Optional
from django.db import models
from domains.commons.BaseService import BaseService
from django.db.models import QuerySet

class BaseController:
    class Meta:
        model: type[models.Model] = None

    service_class: type[BaseService] = None

    def get_all(self, *args, **kwargs) -> QuerySet[models.Model]:
        return self.service_class().get_all(*args, **kwargs)


    def get(self, pk: int, *args, **kwargs) -> Optional[models.Model]:
        return self.service_class().get(pk=pk, *args, **kwargs)
