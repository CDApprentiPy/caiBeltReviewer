"""beltReviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.users import views as users_views

urlpatterns = [
    url(r'^$', users_views.index_page),
    url(r'^users', include('apps.users.urls', namespace='users')),
    url(r'^books', include('apps.books.urls', namespace='books')),
    url(r'^authors', include('apps.authors.urls', namespace='authors')),
    url(r'^reviews', include('apps.reviews.urls', namespace='reviews')),
]
