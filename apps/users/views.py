# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse

from .forms import RegistrationForm
from .models import User

# Create your views here.
def index_page(request):
  context = {
    "registration_form": RegistrationForm()
  }
  return render(request, "users/index.html", context)

# form processes
def create_user(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    form.is_valid()
    User.objects.create(
      name=form.cleaned_data["name"],
      alias=form.cleaned_data["alias"],
      email=form.cleaned_data["email"],
      password=form.cleaned_data["password"]
    )
    return redirect(reverse("books:index_page"))

  return redirect(reverse("users:index_page"))