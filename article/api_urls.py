
from rest_framework_extensions.routers import ExtendedDefaultRouter
from article.viewsets import UserViewSet, PostViewSet, CommentViewSet

router = ExtendedDefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'posts', PostViewSet, basename="posts")
router.register(r'comments', CommentViewSet, basename="comments")
