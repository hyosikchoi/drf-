from django.db import models
from django.db.models import QuerySet
from django.http import Http404
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
            raise Http404(f"{self.Meta.model.__name__} does not exist")
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
                )  # set 메서드를 통해 django orm이 자동으로 매핑 테이블에 id 값들을 many_to_many_value 갯수 만큼 insert 시킨다.
        return row

    def update(self, pk: int, validated_data: dict) -> models.Model:
        try:
            data = validated_data.copy()
            info = model_meta.get_field_info(self.Meta.model)
            many_to_many = {}

            # Many-to-many 필드 분리
            for field_name, relation_info in info.fields.items():
                if relation_info.many_to_many and (field_name in data):
                    many_to_many[field_name] = data.pop(field_name)

            instance = self.get(pk)
            for key, value in validated_data.items(): # 일반 필드 데이터 먼저 update
                setattr(instance, key, value) # 메모리상에서 데이터 변경
            instance.save() # db 에 변경 반영

            # Many-to-many 필드 처리
            if many_to_many:
                for field_name, many_to_many_value in many_to_many.items():
                    field = getattr(instance, field_name)
                    field.set(many_to_many_value)

            return instance
        except ValueError as e:
            raise ValidationError(e)
        except self.Meta.model.DoesNotExist:
            raise Http404(f"{self.Meta.model.__name__} does not exist")

    def delete(self, pk: int, *args, **kwargs):
        instance = self._get_queryset(*args, **kwargs).filter(pk=pk).first()
        if not instance:
            raise Http404(f"{self.Meta.model.__name__} does not exist")
        instance.delete()
