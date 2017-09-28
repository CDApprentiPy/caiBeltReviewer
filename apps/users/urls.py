from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index_page, name='index_page'),
  url(r'^add$', views.CreateUserView.as_view(), name='add'),
  url(r'^login$', views.LoginUserView.as_view(), name='login')
]