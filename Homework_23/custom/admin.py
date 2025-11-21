from django.contrib import admin

from .models import Article, Tag

class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'word_count']
    search_fields = ['title', 'content']
    list_filter = ['metadata']
    actions = ['uppercase_titles']
    inlines = [TagInline]

    def uppercase_titles(self, request, queryset):
        for obj in queryset:
            obj.title = obj.title.upper()
            obj.save()

    uppercase_titles.short_description = "Convert titles to uppercase"
