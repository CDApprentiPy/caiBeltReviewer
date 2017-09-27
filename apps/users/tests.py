from django.urls import resolve
from django.core.urlresolvers import reverse
from django.test import TestCase
import copy

from .views import index_page
from .models import User

# Globals for models and views tests
VALID_USER = {
  "name": "Alice",
  "alias": "alice123",
  "email": "alice@123.com",
  "password": "thisIsAGreatPassword",
  "confirm": "thisIsAGreatPassword"
}

# Models
class UserModel(TestCase):
  def test_save_and_retrieve_user(self):
    User.objects.create(
      name=VALID_USER["name"],
      alias=VALID_USER["alias"],
      email=VALID_USER["email"],
      password=VALID_USER["password"],
    )
    user = User.objects.get(email=VALID_USER["email"])
    self.assertEqual(user.email, VALID_USER["email"])

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
  def test_registration_redirects_if_not_post(self):
    response = self.client.get(reverse("users:create"))
    self.assertEqual(response.status_code, 302)
  
  def test_registration_creates_user_given_valid_data(self):
    response = self.client.post(reverse("users:create"), VALID_USER)
    num_users = User.objects.filter(email=VALID_USER["email"]).count()
    self.assertEqual(num_users, 1)
  
  def test_registration_doesnt_create_given_invalid_data(self):
    INVALID_USER = copy.copy(VALID_USER)
    INVALID_USER["email"] = "somethingInvalid"
    response = self.client.post(reverse("users:create"), INVALID_USER)
    num_users = User.objects.filter(email=INVALID_USER["email"]).count()
    self.assertEqual(num_users, 0)