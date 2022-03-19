from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView

from webapp.models import Article
from webapp.forms import ArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('updated_at')
        return render(request, 'index.html', {'articles': articles})


def create_article_view(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_create.html', {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = form.cleaned_data.get('author')
            new_article = Article.objects.create(title=title, content=content, author=author)
            return redirect("article_view", pk=new_article.pk)
        return render(request, 'article_create.html', {"form": form})


class ArticleView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        context['article'] = article
        return context


def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={
            'title': article.title,
            'content': article.content,
            'author': article.author
        })
        return render(request, 'article_update.html', {"article": article, "form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.author = request.POST.get('author')
            article.save()
            return redirect("article_view", pk=article.pk)
        return render(request, 'article_update.html', {"article": article, "form": form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, 'article_delete.html', {'article': article})
    else:
        article.delete()
        return redirect('index')
