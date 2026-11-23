from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title field
    list_display = ('title', 'category', 'author', 'status', 'is_featured', 'created_at')  # Display these fields in the admin list view
    search_fields = ('id','title', 'category__category_name', 'status')  # Enable search by title, category name, and author username
    list_editable = ('status', 'is_featured')  # Allow editing of status and is_featured fields directly in the list view

admin.site.register(Category)
admin.site.register(Blog , BlogAdmin)  # Register the Blog model with the custom BlogAdmin class