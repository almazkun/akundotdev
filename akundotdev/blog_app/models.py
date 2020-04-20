from django.db import models


import markdown


# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name="Title", max_length=90)
    slug = models.SlugField(verbose_name="Slug", max_length=90, unique=True)
    description = models.CharField(verbose_name="Description", max_length=280)
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)
    content = models.TextField(verbose_name="Content", help_text="Use Markdown syntax")
    views = models.IntegerField(verbose_name="Views", default=0)
    
    class Meta:
        verbose_name = "Article"
        ordering = ["-created_on"]
        
    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def update_views(self):
        self.views += 1
        self.save(update_fields=["views"])
