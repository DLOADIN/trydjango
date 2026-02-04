from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )

from .models import Articles

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Articles.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Articles.objects.all()