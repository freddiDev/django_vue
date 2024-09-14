from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "rating", "published"]
    list_filter = ["title", "published", "rating"]
    search_fields = ["title"]
