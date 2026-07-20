from django.contrib import admin
from.models import Book, Review

class ReviewInline(admin.TabularInline):
    model = Review # FIX 1: you need to tell which model this inline is for
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'added_by', 'created_at'] # FIX 2: 'author' had missing quote
    search_fields = ['title', 'author']
    inlines = [ReviewInline]

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating'] # FIX 3: 'reating' spelling mistake
    list_filter = ['rating']