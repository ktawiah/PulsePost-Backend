from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet

router = SimpleRouter()

router.register("", PostViewSet, "post")

urlpatterns = [
    path("", include(router.urls)),
]
