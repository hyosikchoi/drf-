from django.db import models
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError
from rest_framework.utils import model_meta


class BaseService:
    class Meta:
        model: type[models.Model] = None

    def _get_queryset(self, *args, **kwargs) -> QuerySet:
        return self.Meta.model.objects.order_by("-id")

    def get_all(self, *args, **kwargs) -> QuerySet:
        return self._get_queryset(*args, **kwargs)

    def get(self, pk: int, *args, **kwargs) -> models.Model | None:
        instance = self._get_queryset(*args, **kwargs).filter(pk=pk).first()
        if not instance:
            raise self.Meta.model.DoesNotExist()
        return instance

    def create(self, validated_data: dict) -> models.Model:
        data = validated_data.copy()
        info = model_meta.get_field_info(self.Meta.model)
        many_to_many = {}
        for field_name, relation_info in info.fields.items():
            if relation_info.many_to_many and (field_name in data):
                many_to_many[field_name] = data.pop(field_name)

        row = self.Meta.model(**data)
        row.save()
        if many_to_many:
            for many_to_many_field_name, many_to_many_value in many_to_many.items():
                field = getattr(row, many_to_many_field_name)
                field.set(
                    many_to_many_value
                )  # set 메서드를 통해 매핑 테이블에 many_to_many_value 갯수 만큼 row 를 insert 시킨다.
        return row

    def update(self, pk: int, validated_data: dict) -> models.Model:
        try:
            queryset = self._get_queryset().filter(pk=pk)
            data = validated_data.copy()
            queryset.update(**data)
            return queryset.first()
        except ValueError as e:
            raise ValidationError(e)
        except self.Meta.model.DoesNotExist:
            raise self.Meta.model.DoesNotExist()
