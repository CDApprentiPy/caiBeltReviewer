# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse

import copy

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
    "review_text": "The book and lectures are thought provoking",
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
      text=BOOK_JUSTICE["review"]["review_text"],
      rating=BOOK_JUSTICE["review"]["rating"],
      user=user,
      book=justice_book
    )
    self.assertEqual(review_of_justice_by_user.text, BOOK_JUSTICE["review"]["review_text"])

class AddReviewForm(TestCase):
  def test_loads_add_review_page_on_get(self):
    response = self.client.get(reverse("reviews:add"))
    self.assertTemplateUsed(response, "reviews/add.html")
  
  def test_redirects_to_home_if_not_logged_in(self):
    pass

  def test_redirects_to_reviewed_book_page_on_valid_review_submission(self):
    user = login(self)
    add_book_to_db(BOOK_JUSTICE)
    review_details = copy.copy(BOOK_JUSTICE["review"])
    review_details["book_title"] = BOOK_JUSTICE["title"]
    review_details["author_name"] = BOOK_JUSTICE["author"]["name"]
    response = self.client.post(reverse("reviews:add"), review_details)

    review = Review.objects.get(book__title=review_details["book_title"], book__author__name=review_details["author_name"])
    location = "/books/" + str(review.id)
    self.assertEqual(response["location"], location)

def add_book_to_db(book):
  author = Author.objects.create(
    name=book["author"]["name"]
  )
  book = Book.objects.create(
    title=book["title"],
    author=author
  )
  return book

def login(self):
  try:
    User.objects.get(email=VALID_USER["email"]).delete()
  except:
    pass
  user = User.objects.validate_registration(VALID_USER)
  self.client.post(reverse("users:login"), VALID_USER)
  return user