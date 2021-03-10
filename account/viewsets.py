from django.contrib.auth import get_user_model
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from core.viewsets import BaseModelViewSet
from article import serializers as article_serializer

from . import serializers as account_serializers
from .permissions import UserPermission
User = get_user_model()


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = account_serializers.UserSerializer
    serializer_classes = {
        "posts": article_serializer.PostListSerializer,
    }
    permission_classes = [UserPermission]
    ordering = ["id"]

    @action(methods=["get"], detail=True, url_name="posts", url_path="posts")
    def posts(self, request, *args, **kwargs) -> Response:
        user = self.get_object()
        posts = user.posts.active()
        serializer = self.get_serializer(instance=posts, many=True)
        return Response(
            {
                "count": posts.count(),
                "results": serializer.data,
            }
        )