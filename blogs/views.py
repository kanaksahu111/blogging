from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category

def posts_by_category(request, category_id):
    #fetch posts based on the category_id 
    posts = Blog.objects.filter(status='Published', category=category_id)
    #try:
    #    category = Category.objects.get(pk=category_id)
    #except:
    #    return redirect('home')  # Redirect to home if the category does not exist , can also use 404 page using the get_object_or_404 method
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts' : posts,
        'category_id' : category,
    }
    return render(request, 'posts_by_category.html', context)  # Render the 'posts_by_category.html' template with the provided context