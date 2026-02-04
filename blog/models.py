from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db import models


class Articles(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    content = models.TextField()