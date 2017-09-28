# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.views import View

from .forms import RegistrationForm, LoginForm
from .models import User

# Create your views here.
def index_page(request):
  context = {
    "registration_form": RegistrationForm(),
    "login_form": LoginForm()
  }
  return render(request, "users/index.html", context)

# form processes
class CreateUserView(View):
  fail_template = "users:index_page"
  success_template = "books:index_page"
  
  def get(self, request):
    return redirect(reverse(self.fail_template))

  def post(self, request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
      new_user = User.objects.validate_registration(form.cleaned_data)
      if new_user:
        return redirect(reverse(self.success_template))
    return redirect(reverse(self.fail_template))

class LoginUserView(View):
  fail_template = "users:index_page"
  success_template = "books:index_page"

  def get(self, request):
    return redirect(reverse(self.fail_template))
  
  def post(self, request):
    form = LoginForm(request.POST)
    if form.is_valid():
      user = User.objects.validate_login(form.cleaned_data)
      if user:
        return redirect(reverse(self.success_template))
    return redirect(reverse(self.fail_template))