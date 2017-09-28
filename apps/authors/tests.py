# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Author

# Create your tests here.
VALID_AUTHOR = {
  "name": "Bob"
}

class AuthorModel(TestCase):
  def test_save_and_retrieve_author(self):
    author = Author.objects.create(
      name=VALID_AUTHOR["name"]
    )
    self.assertEqual(author.name, VALID_AUTHOR["name"])