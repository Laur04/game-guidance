from django import forms

class CreateForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(min_length=8, max_length=30, required=True, widget=forms.PasswordInput)
