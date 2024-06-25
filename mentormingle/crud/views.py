from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.urls import reverse, reverse_lazy
from .forms import PostForm
import logging

logger = logging.getLogger(__name__)
""" 
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

 """


class HomeListView(LoginRequiredMixin, ListView):
    model = Post


class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Post


class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("crud:post_home")


class HomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "crud/post_update.html"
    success_url = reverse_lazy("crud:post_home")


class HomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("crud:post_home")
