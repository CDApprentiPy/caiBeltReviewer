# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..authors.models import Author

class BookManager(models.Manager):
  pass

class Book(models.Model):
  objects = BookManager()

  title = models.CharField(max_length=255)
  author = models.ForeignKey(Author, related_name="authored_books")