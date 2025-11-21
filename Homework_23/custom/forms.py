from django import forms

from .models import Article
from .validators import validate_hex


class ArticleForm(forms.ModelForm):
    color = forms.CharField(validators=[validate_hex], required=False,
                            widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Article
        fields = ['title', 'content', 'color']

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']

    def clean_phone_number(self):
        number = self.cleaned_data.get('phone_number')
        if number and not number.isdigit():
            raise ValidationError("Phone number must contain only digits")
        return number
