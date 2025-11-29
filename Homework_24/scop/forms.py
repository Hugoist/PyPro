from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label='Name', max_length=150)
    age = forms.IntegerField(label='Age', min_value=1, max_value=150)
