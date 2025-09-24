from django.urls import include, path
from rest_framework import routers

from apis.common_views import ping
from apis.views.accounts_organization_views import AccountsOrganizationViewSet


router = routers.SimpleRouter()

router.register(r"organizations", AccountsOrganizationViewSet, basename="organizations")

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("", include(router.urls)),
]