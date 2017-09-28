# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AuthorManager(models.Manager):
  pass

class Author(models.Model):
  objects = AuthorManager()

  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

def create_author(data):
  return Author.objects.create(
    name=data["name"]
  )