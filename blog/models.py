from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.db import models


class Articles(models.Model):
    title = models.TextField()
    content = models.TextField()