from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class BoardView(LoginRequiredMixin, ListView):
    template_name = 'board/board.html'
    model = Post
    ordring = '-pub_date'

    context_object_name = 'post_list'

class PostDetail(LoginRequiredMixin, DetailView):
    template_name = 'board/post.html'
    model = Post
    context_object_name = 'post_detail'

class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'board/form.html'
    success_url = reverse_lazy('board:board')
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.contributer = self.request.user.username
        post.save()
        return super().form_valid(form)
