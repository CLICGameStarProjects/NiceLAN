from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe", "class": "form-control"})
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Nom d'utilisateur", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Courriel", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Mot de passe", "class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Répéter le mot de passe", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
