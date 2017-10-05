from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^add$', views.AddReviewView.as_view(), name="add")
]