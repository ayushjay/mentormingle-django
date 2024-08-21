from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeListView,
    HomeDetailView,
    HomeUpdateView,
    HomeDeleteView,
    HomeCreateView,
)
from django.contrib.auth.views import LoginView, LogoutView

app_name = "crud"
urlpatterns = [
    path("", HomeListView.as_view(), name="post_home"),
    path("post/<int:pk>", HomeDetailView.as_view(), name="post_detail"),
    path("post/new", HomeCreateView.as_view(), name="post_create"),
    path("post/update/<int:pk>", HomeUpdateView.as_view(), name="post_update"),
    path("post/delete/<int:pk>", HomeDeleteView.as_view(), name="post_delete"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
