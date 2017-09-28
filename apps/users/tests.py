from django.urls import resolve
from django.core.urlresolvers import reverse
from django.test import TestCase
import copy, re

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
    user = User.objects.create(
      name=VALID_USER["name"],
      alias=VALID_USER["alias"],
      email=VALID_USER["email"],
      password=VALID_USER["password"],
    )
    self.assertEqual(user.email, VALID_USER["email"])
  
  def test_saves_bcrypted_password_to_db(self):
    user = User.objects.validate_registration(VALID_USER)
    BCRYPT_REGEX = re.compile(r"^\$2.\$")
    self.assertTrue(BCRYPT_REGEX.match(user.password))

# Views
class HomePage(TestCase):
  def test_root_url_resolves_to_index_page_view(self):
    found = resolve(reverse("home"))
    self.assertEqual(found.func, index_page)
  
  def test_index_page_returns_correct_html(self):
    response = self.client.get(reverse("home"))
    self.assertTemplateUsed(response, "users/index.html")

# Routes
class RegistrationForm(TestCase):  
  def test_registration_redirects_if_not_post(self):
    response = self.client.get(reverse("users:add"))
    self.assertEqual(response.status_code, 302)
  
  def test_registration_creates_user_given_valid_data(self):
    response = self.client.post(reverse("users:add"), VALID_USER)
    num_users = User.objects.filter(email=VALID_USER["email"]).count()
    self.assertEqual(num_users, 1)
  
  def test_registration_doesnt_create_given_invalid_data(self):
    INVALID_USER = copy.copy(VALID_USER)
    INVALID_USER["email"] = "somethingInvalid"
    response = self.client.post(reverse("users:add"), INVALID_USER)
    num_users = User.objects.filter(email=INVALID_USER["email"]).count()
    self.assertEqual(num_users, 0)

class LoginAndLogout(TestCase):
  def test_invalid_login_redirects_to_home(self):
    # login user that is not in the db
    response = self.client.post(reverse("users:login"), VALID_USER)
    self.assertEqual(response["location"], reverse("home"))
  
  def test_valid_login_redirects_to_books(self):
    # manually add user to test db
    user = User.objects.validate_registration(VALID_USER)
    # login user
    response = self.client.post(reverse("users:login"), VALID_USER)
    self.assertEqual(response["location"], reverse("books:index_page"))
  
  def test_valid_login_adds_user_to_session(self):
    # manually add user to test db
    user = User.objects.validate_registration(VALID_USER)
    # login user
    response = self.client.post(reverse("users:login"), VALID_USER)
    self.assertEqual(self.client.session["user_email"], VALID_USER["email"])
    self.assertEqual(self.client.session["user_alias"], VALID_USER["alias"])

  def test_logout_redirects_to_home(self):
    # manually add user to test db
    user = User.objects.validate_registration(VALID_USER)
    # login user
    login_response = self.client.post(reverse("users:login"), VALID_USER)
    # logout user
    logout_response = self.client.get(reverse("users:logout"))
    self.assertEqual(logout_response["location"], reverse("home"))
  
  def test_logout_removes_user_from_session(self):
    # manually add user to test db
    user = User.objects.validate_registration(VALID_USER)
    # login user
    login_response = self.client.post(reverse("users:login"), VALID_USER)
    # logout user
    logout_response = self.client.get(reverse("users:logout"))
    self.assertFalse(self.client.session["user_email"])
    self.assertFalse(self.client.session["user_alias"])    