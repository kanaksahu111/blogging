
from django.contrib import auth
from django.shortcuts import redirect, render
from blog_main.forms import RegistrationForm
from blogs.models import Blog, Category
from assignments.models import About
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    
    featured_posts = Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='published').order_by('updated_at')

    #fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)  #render is used to get a page 

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  
    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)   

def login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
    form = AuthenticationForm()
    context={
        'form' : form,
    }
    return render(request , 'login.html' , context)

def logout(request):
    auth.logout(request)
    return redirect('home')
