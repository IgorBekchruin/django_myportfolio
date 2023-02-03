import email
from email.policy import default
from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    body = models.TextField(verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add = True)
    time_update = models.DateTimeField(auto_now = True)
    slug = models.SlugField(max_length=200)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    
    def __str__(self):
        return f"Comment {self.description} by {self.name}."
    