# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..users.models import User
from ..books.models import Book
from ..authors.models import Author

class ReviewManager(models.Manager):
  def validate_add_review(self, data):
    errors = {}
    user = find_user_with_email(data["user_email"])
    if not user:
      errors["user_not_found"] = "The user could not be found."
      return None
    book = find_book_with_title_and_author({
      "book_title": data["book_title"],
      "author_name": data["author_name"]
    })
    if not book:
      author = find_author_with_name(data["author_name"])
      if not author:
        Author.objects.create(
          name=data["author_name"]
        )
      Book.objects.create(
        title=data["book_title"],
        author=author
      )
    review = Review.objects.create(
      text=data["review_text"],
      rating=data["rating"],
      user=user,
      book=book
    )
    return review

class Review(models.Model):
  objects = ReviewManager()

  text = models.CharField(max_length=255)
  rating = models.IntegerField()
  user = models.ForeignKey(User, related_name="reviews")
  book = models.ForeignKey(Book, related_name="reviews")

def find_user_with_email(email):
  try:
    return User.objects.get(email=email)
  except:
    return None

def find_author_with_name(author_name):
  try:
    return Author.objects.get(name=author_name)
  except:
    return None

def find_book_with_title_and_author(book):
  try:
    return Book.objects.get(title=book["book_title"], author__name=book["author_name"])
  except:
    return None