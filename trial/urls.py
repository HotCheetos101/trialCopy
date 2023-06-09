"""
URL configuration for trial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

# views.py ni iya pasabot so tanan
from .import views

# gi add para sa css ug images
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # gi include nato ang mga urls ni articles
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', views.about),
    path('base_layout/', views.base_layout),

    path('', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
