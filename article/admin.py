from django.contrib import admin
from django.db.models import Count
from django.db.models.query import prefetch_related_objects
from article import models as article_models

# Register your models here.

class CommentAdminModelInLine(admin.TabularInline):
    model = article_models.Comment
    extra = 1

class LikeAdminModelInLine(admin.TabularInline):
    model = article_models.Like
    extra = 0


@admin.register(article_models.Post)
class PostAdminModel(admin.ModelAdmin):
    inlines = [CommentAdminModelInLine] 
    list_display = ("title", "slug", "created", "user_name", "like_count")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created",)
    list_filter = ("status", "created", )


    def user_name(self, obj):
        return obj.author.username

    def like_count(self, obj):
        return obj.like_count

    def get_queryset(self, request):
        qs = super().get_queryset(request)  

        return (
            qs.prefetch_related("comments")\
            .select_related("author")\
            .annotate(like_count=Count("likes"))
            )


@admin.register(article_models.Comment)
class CommentAdminModel(admin.ModelAdmin):
    list_display = ("author_comment", "post", "created")
    
    ordering = ("-created",)
    list_filter = ("created", "author_comment",)
