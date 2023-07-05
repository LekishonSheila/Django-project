from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.TextField('Category')
    tags = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Comment by {self.author.username} on {self.blog_post.title}"
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
