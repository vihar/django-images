from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.FileField(upload_to="media", null=True, blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.title
