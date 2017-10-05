# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from apps.users.models import User
import time, unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support.wait import WebDriverWait

VALID_USER = {
  "name": "Alice",
  "alias": "alice123",
  "email": "alice@123.com",
  "password": "thisIsAGreatPassword",
  "confirm": "thisIsAGreatPassword"
}

class EndToEnd(StaticLiveServerTestCase):
  @classmethod
  def setUpClass(cls):
    super(EndToEnd, cls).setUpClass()
    cls.selenium = webdriver.Chrome()
    cls.selenium.implicitly_wait(10)
  
  @classmethod
  def tearDownClass(cls):
    cls.selenium.refresh()
    cls.selenium.quit()
    super(EndToEnd, cls).tearDownClass()

  # Website loads
  def test_html_loads(self):
    self.selenium.get(self.live_server_url)
    self.assertIn("Belt Reviewer", self.selenium.title)

  # Presented with login form
  def test_index_view_login_form_loads(self):
    self.selenium.get(self.live_server_url)
    element = self.selenium.find_element_by_id("login-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")

  # Presented with registration form
  def test_index_view_registration_form_loads(self):
    self.selenium.get(self.live_server_url)
    element = self.selenium.find_element_by_id("registration-form")
    self.assertTrue(element)
    self.assertEqual(element.tag_name, "form")
  
  # User is presented with errors messages if registration fails

  # User can register: doesn't work because form submission doesn't use the test db
  def test_user_can_register(self):
    self.register_new_user()
    # time.sleep(3)
    WebDriverWait(self.selenium, 2).until(
      lambda driver: driver.find_element_by_tag_name("body")  
    )
    self.assertEqual(self.selenium.current_url, self.live_server_url + "/books/")

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
  @unittest.skip("")
  def test_user_can_login(self):
    self.register_new_user() # why does this need to be run again?
    self.selenium.get(self.live_server_url)
    form = self.selenium.find_element_by_id("login-form")
    form.find_element_by_name("email").send_keys(VALID_USER["email"])
    form.find_element_by_name("password").send_keys(VALID_USER["password"])
    form.find_element_by_tag_name("button").click()
    time.sleep(3)
    self.assertEqual(self.selenium.current_url, self.live_server_url + "/books/")

  def register_new_user(self):
    self.selenium.get(self.live_server_url)
    form = self.selenium.find_element_by_id("registration-form")
    form.find_element_by_name("name").send_keys(VALID_USER["name"])
    form.find_element_by_name("alias").send_keys(VALID_USER["alias"])
    form.find_element_by_name("email").send_keys(VALID_USER["email"])
    form.find_element_by_name("password").send_keys(VALID_USER["password"])
    form.find_element_by_name("confirm").send_keys(VALID_USER["confirm"])
    form.find_element_by_tag_name("button").click()

if __name__ == "__main__":
  unittest.main()