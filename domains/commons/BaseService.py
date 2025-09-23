from typing import TYPE_CHECKING, Optional
from django.db import models
from django.db.models import QuerySet

class BaseService:
    class Meta:
        model: type[models.Model] = None

    def _get_queryset(self, *args, **kwargs) -> QuerySet:
        return self.Meta.model.objects.order_by('-id')

    def get_all(self, *args, **kwargs) -> QuerySet:
        return self._get_queryset(*args, **kwargs)

    def get(self, pk: int, *args, **kwargs) -> Optional[models.Model]:
        instance = self._get_queryset(*args, **kwargs).filter(pk=pk).first()
        if not instance:
            raise self.Meta.model.DoesNotExist()
        return instance

