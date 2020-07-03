from django.views.generic import ListView, DetailView


import markdown


from .models import Tag, Article


class HomepageListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/home.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/articles.html"


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/article_detail.html"
    
    
    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()
        md = markdown.Markdown(extensions=["markdown.extensions.extra"])
        obj.content = md.convert(obj.content)
        return obj
