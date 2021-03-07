from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post, Comment

from django.urls import reverse
from django.views import generic

from rest_framework import viewsets
from .serializers import * 

from . import forms


class CkEditorFormView(generic.FormView):
    form_class = forms.CkEditorForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse("ckeditor-form")


ckeditor_form_view = CkEditorFormView.as_view()
# Create your views here.


# view
class PostDetailView(DetailView):

    form_class = forms.CkEditorForm
    model = Post
    template_name = "article/post_detail.html"


class PostListView(ListView):
    queryset = Post.objects.draft()
    template_name = "article/index.html"
    
# API
class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

class PostViewSet(viewsets.ModelViewSet):
	serializer_class = PostSerializer
	queryset =Post.objects.all()