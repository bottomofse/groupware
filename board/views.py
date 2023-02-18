from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Post

class BoardView(LoginRequiredMixin, ListView):
    template_name = 'board/board.html'
    model = Post
    ordring = '-pub_date'

    context_object_name = 'post_list'
