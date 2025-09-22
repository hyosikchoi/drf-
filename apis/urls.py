from django.urls import path
from apis.common_views import ping

urlpatterns = [
    path("ping/", ping, name="ping"),
]