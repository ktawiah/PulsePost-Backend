from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer definition for the Post model."""

    url = serializers.HyperlinkedIdentityField(view_name="post_detail", lookup_field="pk", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "url",
            "user",
            "title",
            "content",
            "created_at",
            "updated_at",
            "status",
            "likes",
        ]
