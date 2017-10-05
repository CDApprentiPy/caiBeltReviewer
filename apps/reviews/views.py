# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views import View
import copy

from .forms import AddReviewForm
from .models import Review

class AddReviewView(View):
  def get(self, request):
    context = {
      "add_review_form": AddReviewForm()
    }
    return render(request, "reviews/add.html", context)
  
  def post(self, request):
    form = AddReviewForm(request.POST)
    if form.is_valid():
      data = copy.copy(form.cleaned_data)
      data["user_email"] = request.session["user_email"]
      review = Review.objects.validate_add_review(data)
      if review:
        return redirect(reverse("books:details", kwargs={ "id": review.id }))
    return redirect(reverse("reviews:add"))