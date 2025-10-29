from django.contrib import admin
from .models import Category, Ad, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin panel for categories"""
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """Admin panel for ads with filters and status """
    list_display = ("title", "category", "price", "is_active", "user", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description")
    list_editable = ("is_active",)
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin panel for comments"""
    list_display = ("content", "ad", "user", "created_at")
    search_fields = ("content",)
    list_filter = ("created_at",)
