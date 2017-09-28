# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Review
from ..users.models import User
from ..books.models import Book
from ..authors.models import Author

VALID_USER = {
  "name": "Alice",
  "alias": "alice123",
  "email": "alice@123.com",
  "password": "thisIsAGreatPassword",
  "confirm": "thisIsAGreatPassword"
}
BOOK_JUSTICE = {
  "title": "Justice",
  "author": {
    "name": "Michael Sandel"
  },
  "review": {
    "text": "The book and lectures are thought provoking",
    "rating": 4
  }
}

# Models
class ReviewModel(TestCase):
  def test_save_and_retrieve_review(self):
    justice_author = Author.objects.create(
      name=BOOK_JUSTICE["author"]["name"]
    )
    justice_book = Book.objects.create(
      title=BOOK_JUSTICE["title"],
      author=justice_author
    )
    user = User.objects.create(
      name=VALID_USER["name"],
      alias=VALID_USER["alias"],
      email=VALID_USER["email"],
      password=VALID_USER["password"],
    )

    review_of_justice_by_user = Review.objects.create(
      text=BOOK_JUSTICE["review"]["text"],
      rating=BOOK_JUSTICE["review"]["rating"],
      user=user,
      book=justice_book
    )
    self.assertEqual(review_of_justice_by_user.text, BOOK_JUSTICE["review"]["text"])