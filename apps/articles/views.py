from django.views.generic import ListView


from .models import Tag, Article


class HomepageListView(ListView):
    model = Article
    context_object_name = "article"
    template_name = "articles/home.html"
