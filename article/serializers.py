from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField


from account import serializers as account_serializers
from article import models as article_models


class CommentSerializer(serializers.ModelSerializer):
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=article_models.Post.objects.all(),
        source="post"
    )

    class Meta:
        model = article_models.Comment
        fields = ("id", "post_id", "author_comment", "body",)

class PostListSerializer(serializers.ModelSerializer):
    author = account_serializers.UserSerializer(read_only=True)
    status = serializers.ChoiceField(
        choices=article_models.POST_STATUS,
        default="draft",
        required=False
    )

    class Meta:
        model = article_models.Post
        fields = (
            "id",
            "slug",
            "title",
            "status",
            "created",
            "author"
        )


class PostSerializer(PostListSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        source="author",
    )
    comments = CommentSerializer(many=True, read_only=True)
    like_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = article_models.Post
        fields = (
            "id",
            "slug",
            "title",
            "body",
            "created",
            "updated",
            "status",
            "author_id",
            "author",
            "like_count",
            "comments",
        )
