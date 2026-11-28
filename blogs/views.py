from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.db.models import Q

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

def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published') 
    context = {
        'single_blog' : single_blog,
    }
    return render(request , 'blogs.html' , context)

def search(request):
    keyword = request.GET.get('keyword')  # Retrieve the 'keyword' parameter from the GET request
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published') 

    context = {
        'blogs' : blogs,
        'keyword' : keyword,
    } 
    return render(request, 'search.html' , context)