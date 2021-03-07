from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from article import models as article_models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = article_models.Post
        fields = ('author', 'title', 'body', 'status', 'slug', 'created', 'updated')

