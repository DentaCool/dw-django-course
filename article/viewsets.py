
from rest_framework import viewsets
from django.db.models import Count
from django.contrib.auth.models import User

from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_extensions.mixins import NestedViewSetMixin

from core.viewsets import BaseModelViewSet, BaseReadOnlyViewSet

from account import serializers as account_serializers
from .filtres import *
from .models import *
from .serializers import * 
from .permissions import *


class PostModelViewSet(BaseModelViewSet):
    serializer_class = PostSerializer
    serializer_classes = {
        "list": PostListSerializer,
    }
    queryset = article_models.Post.objects.annotate(like_count=Count("likes")).prefetch_related("comments", "author")
    
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = [PostPermission]

    @action(
        methods=["get"],
        detail=False,
        url_name="current",
        url_path="current",
        permission_classes=[IsAuthenticated]
    )
    def current(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)


    @action(methods=["post"], detail=True, url_path="like", permission_classes=[AllowAny])
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        # session = request.session.session_key
        session_key = request.data.get(
            'session_key',
            request.session.session_key or request.META.get('REMOTE_ADDR')
        )
        if session_key is not None:
            if liked_post := post.likes.filter(session_key=session_key).first():
                liked_post.delete()
            else:
                article_models.Like.objects.create(session_key=session_key, post=post)

        return Response({"like_count": post.likes.count()})


class CommentViewSet(NestedViewSetMixin, viewsets.ModelViewSet, BaseReadOnlyViewSet, CreateModelMixin):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [CommentPermission]
    def get_serializer(self, *args, **kwargs):
        if kwargs.get("data"):
            kwargs["data"].update(self.get_parents_query_dict())
        return super(CommentViewSet, self).get_serializer(*args, **kwargs)

