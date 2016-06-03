from django.contrib import admin
from article.models import Author, Tag, Classification, Article, SayHello


# Register your models here.
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(SayHello)

class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
                '/static/tinymce/tinymce.min.js',
                '/static/tinymce/config.js',
                )
admin.site.register(Article, ArticleAdmin)
