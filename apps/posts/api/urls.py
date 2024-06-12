from django.urls import path

from .views import PostViewSet

post_list = PostViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

post_detail = PostViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("", post_list, name="post_list"),
    path("<str:pk>/", post_detail, name="post_detail"),
]
