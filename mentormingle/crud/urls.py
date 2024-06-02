from django.contrib import admin
from django.urls import path, include
from .views import HomeListView, HomeDetailView, HomeUpdateView, HomeDeleteView

app_name = "crud"
urlpatterns = [
    path("", HomeListView.as_view(), name="post_home"),
    path("post/<int:pk>", HomeDetailView.as_view(), name="post_detail"),
    path("post/update/<int:pk>", HomeUpdateView.as_view(), name="post_update"),
    path("post/delete/<int:pk>", HomeDeleteView.as_view(), name="post_delete"),
]
