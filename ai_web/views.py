from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def index(response):
    title_article = "Artykuły"
    articles = Article.objects.all()
    options = ["opcja 1", "opcja 2"]

    return render(response, "articles.html",
                  {'title_article_view': title_article, "options": options,
                   "articles": articles
                   })


def test_orm(response):
    query = Article.objects.filter(title="kokoko")()
    return HttpResponse(query)
