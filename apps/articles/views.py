from django.views.generic import ListView, DetailView


import markdown


from .models import Tag, Article


class HomepageListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/home.html"
    queryset = Article.objects.all().is_published()[:5]


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/articles.html"
    queryset = Article.objects.all().is_published()


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()
        obj.content = obj.content_to_markdown()
        return obj
