from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from article import models as article_models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = article_models.Comment
        fields = ('id', 'author_comment', 'body')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = article_models.Post
        fields = ('author', 'title', 'body', 'status', 'slug', 'created', 'updated', 'likes')
        comments = CommentSerializer(many=True)


