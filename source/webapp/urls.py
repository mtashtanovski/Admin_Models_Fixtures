from django.urls import path

from webapp.views import index_view, create_article_view, article_view

urlpatterns = [
    path('', index_view),
    path('article/add/', create_article_view),
    path('article/<int:pk>/', article_view)
]
