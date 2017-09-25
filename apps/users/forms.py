from django import forms

class RegistrationForm(forms.Form):
  name = forms.CharField(max_length=255)
  alias = forms.CharField(max_length=255)
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  confirm = forms.CharField(widget=forms.PasswordInput)