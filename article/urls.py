from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post_detail<slug:slug>/', PostDetailView.as_view(), name=('post_detail')),
]


