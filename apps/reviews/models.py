# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..users.models import User
from ..books.models import Book

class ReviewManager(models.Manager):
  pass

class Review(models.Model):
  objects = ReviewManager()

  text = models.CharField(max_length=255)
  rating = models.IntegerField()
  user = models.ForeignKey(User, related_name="reviews")
  book = models.ForeignKey(Book, related_name="reviews")