from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from .models import Post

class BoardView(LoginRequiredMixin, ListView):
    template_name = 'board/board.html'
    model = Post
    ordring = '-pub_date'

    context_object_name = 'post_list'

class PostView(LoginRequiredMixin, DetailView):
    template_name = 'board/post.html'
    model = Post
    context_object_name = 'post_detail'
