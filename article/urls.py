from django.urls import path, include
from .views import PostListView, PostDetailView
from .api_urls import router

urlpatterns = [
    path('', PostListView.as_view()),
    path('post_detail<slug:slug>/', PostDetailView.as_view(), name=('post_detail')),
    path('api/', include(router.urls), name=('api'))
]


urlpatterns+=router.urls