from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^add$', views.create_author, name="create")
]