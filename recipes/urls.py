"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from authe.urls import urlpatterns as auth_urls
from blogs.urls import urlpatterns as blog_urls
from recipe_apps.urls import urlpatterns as recipe_urls
from recipe_profiles.urls import urlpatterns as profile_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += auth_urls
urlpatterns += blog_urls
urlpatterns += recipe_urls
urlpatterns += profile_urls
