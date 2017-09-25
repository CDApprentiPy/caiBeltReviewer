from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from books.views import index_page

class HomePage(TestCase):
  
  def test_root_url_resolves_to_index_page_view(self):
    found = resolve("/")
    self.assertEqual(found.func, index_page)
  
  def test_index_page_returns_correct_html(self):
    response = self.client.get("/")
    html = response.content.decode("utf8")
    self.assertTemplateUsed(response, "books/index.html")