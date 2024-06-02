from django.db import models
from taggit.managers import TaggableManager


class Mentor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    user_bio = models.TextField(max_length=500)
    expertise = TaggableManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300)
    author = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
