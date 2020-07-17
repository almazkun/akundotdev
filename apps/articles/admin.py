from django.contrib import admin


from .models import Tag, Article

# Register your models here.




class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "views", "is_published", "created_on"]

    list_filter = ["views", "is_published", "created_on"]
    list_editable = ["is_published"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
