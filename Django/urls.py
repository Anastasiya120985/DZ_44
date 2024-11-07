"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from Django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('news/', views.news, name='news'),
    path('news/<path:wrong>', views.news_, name='news_'),
    path('management/', views.management, name='management'),
    path('management/<path:wrong>', views.management_, name='management_'),
    path('history/', views.history, name='history'),
    path('history/people/', views.people, name='people'),
    path('history/photos/', views.photos, name='photos'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<path:wrong>', views.contacts_, name='contacts_')
]
