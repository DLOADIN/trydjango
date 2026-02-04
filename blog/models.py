from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db import models
from django.urls import reverse
class Articles(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("articles:article-detail:", kwargs={"id": self.id})  # pylint: disable=no-member