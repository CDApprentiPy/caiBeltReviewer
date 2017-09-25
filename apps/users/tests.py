from django.urls import resolve
from django.core.urlresolvers import reverse
from django.test import TestCase

from .views import index_page
from .models import User

# Globals for models and views tests
name = "Alice"
alias = "alice123"
email = "alice@123.com"
password = "thisIsAGreatPassword"

# Models
class UserModel(TestCase):
  def test_save_and_retrieve_user(self):
    User.objects.create(
      name=name,
      alias=alias,
      email=email,
      password=password,
    )
    user = User.objects.get(name=name)
    self.assertEqual(user.name, name)

# Views
class HomePage(TestCase):
  def test_root_url_resolves_to_index_page_view(self):
    found = resolve(reverse("users:index_page"))
    self.assertEqual(found.func, index_page)
  
  def test_index_page_returns_correct_html(self):
    response = self.client.get(reverse("users:index_page"))
    html = response.content.decode("utf8")
    self.assertTemplateUsed(response, "users/index.html")

# Routes
class RegistrationForm(TestCase):
  registration_form_data = {
    "name": name,
    "alias": alias,
    "email": email,
    "password": password,
    "confirm": password
  }

  def test_registration_can_save_post_request(self):
    response = self.client.post(reverse("users:create"), self.__class__.registration_form_data)
    self.assertEqual(response.status_code, 302)
  
  def test_registration_redirects_if_not_post(self):
    response = self.client.get(reverse("users:create"))
    self.assertEqual(response.status_code, 302)
  
  def test_registration_creates_new_db_user(self):
    response = self.client.post(reverse("users:create"), self.__class__.registration_form_data)
    user = User.objects.get(name=name)
    self.assertEqual(user.name, name)