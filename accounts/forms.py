from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(label="First name", max_length=40)
    last_name = forms.CharField(label="Last name", max_length=40)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


class EditUserForm(forms.Form):

    username = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(
        label="First name", max_length=40, required=False
        )
    last_name = forms.CharField(
        label="Last name", max_length=40, required=False
        )

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email'
        ]


class EditUserPasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        initial='',
        required=False
        )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput,
        initial='',
        required=False
    )

    class Meta:
        model = User
        fields = [
            'password1', 'password2'
        ]
