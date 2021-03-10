from django.db import models
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

user = get_user_model()

POST_STATUS = (("draft", "Draft"),
               ("publish", "Publish"))

class PostQuerySet(models.QuerySet):

    def draft(self):
        return self.filter(status="draft")
    
    def publish(self):
        return self.filter(status="publish")


class PostManager(models.Manager):

    def get_queryset(self):
        return PostQuerySet(self.model)

    def draft(self):
        return self.get_queryset().draft()

    def publish(self):
        return self.get_queryset().publish()


# Create your models here.
class Post(models.Model):
    # on_delete = ["RESTRICT", "DO_NOTHING", "NONE..]
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    body = RichTextField()
    status = models.CharField(max_length=20, choices=POST_STATUS, default="draft")
    slug = models.SlugField(max_length=100, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


    objects = PostManager()

    class Meta:
        default_related_name = ""
        ordering = ("created",)

    def __str__(self):
        return f"{self.title}"



class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author_comment = models.CharField(max_length=50)
    body = models.TextField(max_length=250)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "comments"
        ordering = ("created",)

    def __str__(self):
        return f"{self.body}"


class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="likes")
    # author = models.ForeignKey(user, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = "likes"
        unique_together = (("post", "session_key"),)
