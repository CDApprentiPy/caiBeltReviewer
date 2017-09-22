from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from books.views import index_page

class HomePage(TestCase):
  
  def test_root_url_resolves_to_index_page_view(self):
    found = resolve("/")
    self.assertEqual(found.func, index_page)
  
  def test_index_page_returns_html(self):
    request = HttpRequest()
    response = index_page(request)
    html = response.content.decode("utf8")
    self.assertTrue(html.startswith("<!DOCTYPE html>"))
    self.assertTrue(html.endswith("</html>"))
