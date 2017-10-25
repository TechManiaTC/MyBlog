# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-created_time']
