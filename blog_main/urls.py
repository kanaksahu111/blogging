"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin   #django.contrib is a collection of Django's built-in application, admin is Django's built-in administration application.
from django.urls import path      #path() is a function used to define URL patterns.
from . import views               #The . means the current Python package, which is blog_main in this case. The views module is imported from the current package, allowing access to the view functions defined in blog_main/views.py.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
