from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    """
    a class based for show index page
    """
    template_name = 'index.html'

class PostList(LoginRequiredMixin, ListView):
    """
    this class for show list blog
    """
    queryset = Post.objects.all()
    ordering = '-id'
    paginate_by = 3
    context_object_name = 'posts'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post

class PostCreatedView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'content', 'status', 'category', 'published_date']
    success_url = '/blog/'
    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['author', 'image', 'title', 'content', 'status', 'category', 'published_date']
    success_url = '/blog/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/'
