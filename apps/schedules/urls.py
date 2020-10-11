from django.urls import include, path
from apps.schedules.views import EventViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("event", EventViewSet, basename="event-view-set")
urlpatterns = [path("", include(router.urls))]
