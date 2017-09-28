# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from apps.users.models import User
import time
import unittest

ROOT_URL = "http://127.0.0.1:8000"
VALID_USER = {
  "name": "Alice",
  "alias": "alice123",
  "email": "alice@123.com",
  "password": "thisIsAGreatPassword",
  "confirm": "thisIsAGreatPassword"
}

class EndToEnd(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.get(ROOT_URL)
  
  def tearDown(self):
    self.browser.refresh()
    self.browser.quit()

  # Website loads
  @unittest.skip("")
  def test_html_loads(self):
    self.assertIn("Belt Reviewer", self.browser.title)

  # Presented with login form
  @unittest.skip("")
  def test_index_view_login_form_loads(self):
    element = self.browser.find_element_by_id("login-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # Presented with registration form
  @unittest.skip("")
  def test_index_view_registration_form_loads(self):
    element = self.browser.find_element_by_id("registration-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")
  
  # User is presented with errors messages if registration fails

  # User can register: doesn't work because form submission doesn't use the test db
  # def test_user_can_register(self):
  #   self.register_new_user()
  #   time.sleep(3)
  #   self.assertEqual(self.browser.current_url, ROOT_URL + "/books/")

  # User can log in
  @unittest.skip("")
  def test_user_can_login(self):
    self.register_new_user()
    self.browser.get(ROOT_URL)
    # should create the user in the db first, but doesn't work
    # because form submission doesn't use the test db
    form = self.browser.find_element_by_id("login-form")
    form.find_element_by_name("email").send_keys(VALID_USER["email"])
    form.find_element_by_name("password").send_keys(VALID_USER["password"])
    form.find_element_by_tag_name("button").click()
    time.sleep(3)
    self.assertEqual(self.browser.current_url, ROOT_URL + "/books/")

  def register_new_user(self):
    form = self.browser.find_element_by_id("registration-form")
    form.find_element_by_name("name").send_keys(VALID_USER["name"])
    form.find_element_by_name("alias").send_keys(VALID_USER["alias"])
    form.find_element_by_name("email").send_keys(VALID_USER["email"])
    form.find_element_by_name("password").send_keys(VALID_USER["password"])
    form.find_element_by_name("confirm").send_keys(VALID_USER["confirm"])
    form.find_element_by_tag_name("button").click()

  # User is presented with a list of the latest three book reviews

  # User is also presented with a list of all books with reviews

  # User has the option to add a book review or logout

  # User can add a book review

  # User is redirected to the book's review page after adding one

  # A book review has a rating, review text, and a time stamp

  # User can view user profiles

  # User can return home from user profile page, add book review page, view book review page

  # User can log out

if __name__ == "__main__":
  unittest.main()