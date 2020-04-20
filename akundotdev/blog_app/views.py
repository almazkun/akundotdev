from django.shortcuts import render
from django.views import generic


from .models import Article

import markdown

class ListView(generic.ListView):
    model = Article
    template_name = "articles.html"
    context_object_name = "articles"


class DetailView(generic.DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_object(self):
        obj = super(DetailView, self).get_object()
        obj.update_views()

        md = markdown.Markdown(extensions=["markdown.extensions.extra"])
        obj.content = md.convert(obj.content)

        return obj
# Create your views here.
