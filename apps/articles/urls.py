from django.urls import path


from .views import HomepageListView, ArticleListView, ArticleDetailView


urlpatterns = [
    path("", HomepageListView.as_view(), name="home"),
    path("articles/", ArticleListView.as_view(), name="articles"),
    path("articles/<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
]
