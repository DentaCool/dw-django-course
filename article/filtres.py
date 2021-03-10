import django_filters
from django_filters import rest_framework as filters
from rest_framework import generics
from .models import *


class PostFilter(django_filters.FilterSet):
    # limit = django_filters.RangeFilter(field_name="id")

    class Meta:
        model = Post
        fields = (
            "id",
            "slug",
            "title",
            "status",
            "created",
            "author"
        )


