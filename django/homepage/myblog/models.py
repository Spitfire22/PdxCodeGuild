
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField('Published', auto_created=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    author = models.ForeignKey(User)
    text = models.TextField()
    post = models.ForeignKey(BlogPost)

    def __str__(self):
        return self.author
