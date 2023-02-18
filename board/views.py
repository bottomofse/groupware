from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm, PostUpdateForm

class PostList(LoginRequiredMixin, ListView):
    template_name = 'board/list.html'
    model = Post
    ordring = '-pub_date'

    context_object_name = 'post_list'

class PostDetail(LoginRequiredMixin, DetailView):
    template_name = 'board/detail.html'
    model = Post
    context_object_name = 'post_detail'

class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'board/create.html'
    success_url = reverse_lazy('board:post_list')
    form_class = PostForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.contributer = self.request.user.username
        post.save()
        return super().form_valid(form)

class PostUpdate(UpdateView):
    template_name = 'board/update.html'
    model = Post
    form_class = PostUpdateForm

    def get_success_url(self):
        return reverse_lazy('board:post_detail', kwargs={'pk':self.kwargs['pk']})

class PostDelete(DeleteView):
    template_name = 'board/delete.html'
    model = Post
    success_url = reverse_lazy('board:post_list')
