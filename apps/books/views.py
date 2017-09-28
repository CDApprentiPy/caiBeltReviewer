# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import View

from .models import Book
from ..reviews.models import Review

def index_page(request):
  if request.session["user_email"]:
    # get all books in the db
    context = {
      "books": Book.objects.all(),
      "reviews": Review.objects.all()
    }
    return render(request, "books/index.html", context)
  return redirect("home")