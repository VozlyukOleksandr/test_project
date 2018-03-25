from django import forms

class registration_form(forms.Form):
    nik_name=forms.CharField(max_length=100)
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput, max_length=30)

class login_form(forms.Form):
    nik_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)