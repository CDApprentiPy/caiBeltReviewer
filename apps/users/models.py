# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt, re

class UserManager(models.Manager):
  EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

  def validate_registration(self, data):
    errors = {}
    found_users = find_user_with_email(data["email"])
    if len(found_users):
      errors["email_taken"] = "That email has already been used to register an account."
    if data["password"] != data["confirm"]:
      errors["confirm_password"] = "Passwords must match."

    if not errors:
      return create_user(data)
    else:
      # add errors to messages
      return None

class User(models.Model):
  objects = UserManager()

  name = models.CharField(max_length=255)
  alias = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.email

def create_user(data):
  alias = data["alias"]
  if len(data["alias"]) < 1:
    alias = data["name"]

  return User.objects.create(
    name=data["name"],
    alias=alias,
    email=data["email"],
    password=encrypt_password(data["password"])
  )

def find_user_with_email(email):
  return User.objects.filter(email=email)

def encrypt_password(password):
  return bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())