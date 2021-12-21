from django.urls import path

from webapp.views import index_view, create_article_views, article_view

urlpatterns = [
    path('', index_view),
    path('articles/add/', create_article_views),
    path('article/', article_view)
]
