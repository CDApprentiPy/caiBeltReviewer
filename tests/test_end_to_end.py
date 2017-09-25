# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

ROOT_URL = "http://localhost:8000"

class EndToEnd(unittest.TestCase):
  name = "Alice"
  alias = "alice123"
  email = "alice@123.com"
  password = "thisIsAGreatPassword"

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.get(ROOT_URL)
  
  def tearDown(self):
    self.browser.quit()

  # Website loads
  def test_html_loads(self):
    self.assertIn("Belt Reviewer", self.browser.title)

  # Presented with login form
  def test_index_view_login_form_loads(self):
    element = self.browser.find_element_by_id("login-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # Presented with registration form
  def test_index_view_registration_form_loads(self):
    element = self.browser.find_element_by_id("registration-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # User registers an account
  def test_user_can_register_new_account(self):
    form = self.browser.find_element_by_id("registration-form")
    form.find_element_by_name("name").send_keys(self.__class__.name)
    form.find_element_by_name("alias").send_keys(self.__class__.alias)
    form.find_element_by_name("email").send_keys(self.__class__.email)
    form.find_element_by_name("password").send_keys(self.__class__.password)
    form.find_element_by_name("confirm").send_keys(self.__class__.password)
    form.find_element_by_tag_name("button").click()
    time.sleep(3)
    # user should now be logged in
    self.assertEqual(self.browser.current_url, ROOT_URL + "/books")

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