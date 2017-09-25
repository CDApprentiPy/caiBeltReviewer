# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class EndToEnd(unittest.TestCase):
  name = "Alice"
  alias = "alice123"
  email = "alice@123.com"
  password = "thisIsAGreatPassword"

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.get("http://localhost:8000")
  
  def tearDown(self):
    self.browser.quit()

  # Website loads
  @unittest.skip("skip: test_html_loads")
  def test_html_loads(self):
    self.assertIn("Belt Reviewer", self.browser.title)

  # Presented with login form
  @unittest.skip("skip: test_index_view_login_form_loads")
  def test_index_view_login_form_loads(self):
    element = self.browser.find_element_by_id("login-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # Presented with registration form
  @unittest.skip("skip: test_index_view_registration_form_loads")
  def test_index_view_registration_form_loads(self):
    element = self.browser.find_element_by_id("registration-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # User registers an account
  def test_user_can_register_new_account(self):
    pass

  # User is presented with a list of the latest three book reviews

  # User is also presented with a list of all books with reviews

  # User has the option to add a book review or logout

  # User can add a book review

  # User is redirected to the book's review page after adding one

  # A book review has a rating, review text, and a time stamp

  # User can view user profiles

  # User can return home from user profile page, add book review page, view book review page

  # User can log out

  # User can log in

if __name__ == "__main__":
  unittest.main()