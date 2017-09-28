# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt, re

class UserManager(models.Manager):
  def validate_registration(self, data):
    errors = {}
    user = find_user_with_email(data["email"])
    if user:
      errors["email_taken"] = "That email has already been used to register an account."
    if data["password"] != data["confirm"]:
      errors["confirm_password"] = "Passwords must match."

    if not errors:
      return create_user(data)
    else:
      print "ERRORS:", errors
      # TODO: add errors to messages
      return None
  
  def validate_login(self, data):
    errors = {}
    user = find_user_with_email(data["email"])
    if user:
      if is_valid_password(data["password"], user.password):
        return user
      else:
        errors["incorrect_password"] = "Password is incorrect."
    else:
      errors["unknown_user"] = "A user with that email was not found."
    # TODO: add errors to messages
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
  try:
    return User.objects.get(email=email)
  except:
    return None

def encrypt_password(password):
  return bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())

def is_valid_password(inputPW, encryptedPW):
  return bcrypt.checkpw(str(inputPW).encode(), str(encryptedPW).encode())