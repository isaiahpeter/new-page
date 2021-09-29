from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView) # new
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
class BlogDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'
class BlogCreateView(LoginRequiredMixin, CreateView):
    model= Post
    template_name = 'post_new.html'
    fields = ('title', 'body',)
    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)
class BlogUpdateView(LoginRequiredMixin, UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ('title', 'body')
class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
