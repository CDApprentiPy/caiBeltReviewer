from django import forms

class AddReviewForm(forms.Form):
  book_title = forms.CharField(max_length=255, label="Title")
  author_name = forms.CharField(max_length=255, label="Author")
  review_text = forms.CharField(max_length=1000, label="Review", widget=forms.Textarea)
  rating = forms.IntegerField(min_value=0, max_value=5)