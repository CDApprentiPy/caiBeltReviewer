# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
import unittest

class SomeTest(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome()
  
  def tearDown(self):
    self.browser.quit()

  # Website loads
  def test_html_loads(self):
    self.browser.get("http://localhost:8000")
    self.assertIn("Belt Reviewer", self.browser.title)

# Presented with registration and login forms

# User registers an account

# User is presented with a list of the latest three book reviews

# User is also presented with a list of all books with reviews

# User has the option to add a book review or logout

# User can add a book review

# User is redirected to the book's review page after adding one

# A book review has a rating, review text, and a time stamp

# User can view user profiles

# User can return home from user profile page, add book review page, view book review page

if __name__ == "__main__":
  unittest.main()