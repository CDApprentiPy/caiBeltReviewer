from django.core.urlresolvers import reverse
from django.test import TestCase
from django.http import HttpRequest

from .models import Book
from ..authors.models import Author

BOOK_JUSTICE = {
  "title": "Justice",
  "author": {
    "name": "Michael Sandel"
  }
}

class BookModel(TestCase):
  def test_save_and_retrieve_book(self):
    justice_author = Author.objects.create(
      name=BOOK_JUSTICE["author"]["name"]
    )

    justice_book = Book.objects.create(
      title=BOOK_JUSTICE["title"],
      author=justice_author
    )
    self.assertEqual(justice_book.title, BOOK_JUSTICE["title"])
    self.assertEqual(justice_book.author.name, BOOK_JUSTICE["author"]["name"])