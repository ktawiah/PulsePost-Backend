from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.posts.api.serializers import PostSerializer
from apps.posts.models import Post


class PostViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def list(self, request: Request) -> Response:
        paginator = PageNumberPagination()
        if request.query_params.get("page_size"):
            paginator.page_size = request.query_params.get("page_size")
        else:
            paginator.page_size = 10

        queryset = get_list_or_404(Post.objects.order_by("-updated_at"))
        instance = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(instance=instance, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)

    def create(self, request: Request) -> Response:
        serializer = PostSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Post.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(instance, data=request.data, context={"request": request})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Post.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(instance, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Post.objects.all()
        instance = get_object_or_404(queryset, pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=False)
    def recent_posts(self, request: Request) -> Response:
        paginator = PageNumberPagination()
        if request.query_params.get("page_size"):
            paginator.page_size = request.query_params.get("page_size")
        else:
            paginator.page_size = 10

        queryset = get_list_or_404(Post.objects.all().order_by("-updated_at"))
        instance = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(instance, many=True, context={"request": request})
        return paginator.get_paginated_response(serializer.data)
