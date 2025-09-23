from typing import TYPE_CHECKING

from rest_framework.viewsets import GenericViewSet
from apis.controllers.accounts_organization_controller import BaseController


class BaseViewSet(GenericViewSet):
    serializer_class = None
    controller_class: BaseController = None