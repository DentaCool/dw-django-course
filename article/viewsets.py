
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import * 



class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	queryset = Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()