from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index_page, name='index_page'),
  url(r'^create$', views.create_user, name='create')
]