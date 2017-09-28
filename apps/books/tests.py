from django.core.urlresolvers import reverse
from django.test import TestCase
from django.http import HttpRequest

import copy

from .models import Book
from ..authors.models import Author
from ..users.models import User
from ..reviews.models import Review

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

class BookModel(TestCase):
  def test_save_and_retrieve_book(self):
    book = add_book_to_db(BOOK_JUSTICE)
    self.assertEqual(book.title, BOOK_JUSTICE["title"])
    self.assertEqual(book.author.name, BOOK_JUSTICE["author"]["name"])

class BooksIndexPage(TestCase):
  def test_redirects_to_home_if_user_is_not_logged_in(self):
    # make sure no user is logged in
    self.client.get(reverse("users:logout"))
    response = self.client.get(reverse("books:index_page"))
    self.assertEqual(response["location"], reverse("home"))
  
  def test_db_books_are_displayed(self):
    book = add_book_to_db(BOOK_JUSTICE)
    login(self)
    response = self.client.get(reverse("books:index_page"))
    html = response.content.decode("utf8")
    self.assertIn(book.title, html)

  def test_db_reviews_are_displayed(self):
    # clear the reviews in the db
    try:
      Review.objects.all().delete()
    except:
      pass
    
    user = login(self)
    book = add_book_to_db(BOOK_JUSTICE)

    review_details = copy.copy(BOOK_JUSTICE)
    review_details["review"]["user"] = user
    review_details["review"]["book"] = book
    review = add_review_to_db(review_details)

    expected_string = str(user.alias) + " says: " + str(review.text)

    response = self.client.get(reverse("books:index_page"))
    html = response.content.decode("utf8")
    self.assertIn(expected_string, html)

def add_book_to_db(book):
  author = Author.objects.create(
    name=book["author"]["name"]
  )
  book = Book.objects.create(
    title=book["title"],
    author=author
  )
  return book

def add_review_to_db(details):
  review = Review.objects.create(
    text=details["review"]["text"],
    rating=details["review"]["rating"],
    user=details["review"]["user"],
    book=details["review"]["book"]
  )
  return review

def login(self):
  try:
    User.objects.get(email=VALID_USER["email"]).delete()
  except:
    pass
  user = User.objects.validate_registration(VALID_USER)
  self.client.post(reverse("users:login"), VALID_USER)
  return user