from django import forms

class RegistrationForm(forms.Form):
  name = forms.CharField(max_length=255)
  alias = forms.CharField(max_length=255, required=False)
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  confirm = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
