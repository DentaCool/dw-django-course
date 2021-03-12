from django.urls import path, include
from .views import PostListView, PostDetailView
from .urls_api import router

urlpatterns = [
    path('', PostListView.as_view()),
    path('alternative_index/', PostListView.as_view(), name=('alternative')),
    path('post_detail<slug:slug>/', PostDetailView.as_view(), name=('post_detail')),
 ]


urlpatterns+=router.urls