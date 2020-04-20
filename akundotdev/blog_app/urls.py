from django.urls import path

from .views import ListView, DetailView


urlpatterns = [
    path("articles/", ListView.as_view(), name="articles"),
    path("articles/<slug:slug>/", DetailView.as_view(), name="article_detail"),
]