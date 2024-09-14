from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "published"]
    list_filter = ["title", "published", "price"]
    search_fields = ["title"]
