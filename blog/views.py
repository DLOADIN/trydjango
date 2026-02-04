from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    )

from .models import Articles
from .forms import ArticleForm

class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm
    queryset = Articles.objects.all() # pylint: disable=no-member
class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Articles.objects.all()  # pylint: disable=no-member

class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    queryset = Articles.objects.all()  # pylint: disable=no-member

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Articles, id=id_)