from django.views.generic import ListView, DetailView, TemplateView

import markdown

from apps.users.models import CustomUser
from apps.tools.models import Tool
from apps.shop.models import Product
from .models import Tag, Article


class HomepageListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/home.html"
    queryset = Article.objects.all().is_published()[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        context["tools"] = Tool.objects.all()[:5]
        context["products"] = Product.objects.all()[:5]
        return context


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/articles.html"
    queryset = Article.objects.all().is_published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()
        obj.content = obj.content_to_markdown()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        return context


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = "articles/tag_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_author"] = CustomUser.objects.filter(main_user=True).first()
        context["articles"] = self.object.article_set.all()
        context["tools"] = self.object.tool_set.all()
        context["products"] = self.object.product_set.all()
        return context
