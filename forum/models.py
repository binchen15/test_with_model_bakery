from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Journal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title   = models.CharField(max_length=255)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body    = models.TextField(max_length=10000)

    def __str__(self):
        return "{}-{}".format(self.journal, self.title)
