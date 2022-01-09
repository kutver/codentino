"""codentino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.flatpages import views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include, re_path
from django.shortcuts import redirect
from codentino.apps.blog.models import Post
from codentino.settings import ADMIN_PATH

posts_sitemap_info = {
    'queryset': Post.objects.filter(published='1').order_by('-updated_at'),
    'date_field': 'updated_at',
}

urlpatterns = [
    path('', lambda request: redirect('blog/', permanent=False)),
    path('blog/', include(('codentino.apps.blog.urls', 'blog'), namespace='blog')),
    path('tags/', include(('codentino.apps.tag.urls', 'tag'), namespace='tag')),
    path(ADMIN_PATH, admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('martor/', include('martor.urls')),
    path('sitemap.xml', sitemap, 
        {'sitemaps': {'blog': GenericSitemap(posts_sitemap_info, priority=0.9, changefreq='yearly', protocol='https')}},
        name='django.contrib.sitemaps.views.sitemap'),
    
    # "catchall" pattern for flatpages, hence, 
    # it is important to place the pattern at the end of the other urlpatterns
    re_path(r'^(?P<url>.*/)$', views.flatpage),
]
