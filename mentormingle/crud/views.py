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


class HomeListView(LoginRequiredMixin, ListView):
    model = Post


class HomeDetailView(LoginRequiredMixin, DetailView):
    model = Post


class HomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("crud:post_home")


class HomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("crud:post_home")
