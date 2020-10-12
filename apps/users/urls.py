from django.urls import include, path
from rest_framework import routers
from apps.users.views import UserViewSet


router = routers.DefaultRouter()
router.register("", UserViewSet, basename="user-view-set")
urlpatterns = [path("", include(router.urls))]
