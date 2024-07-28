from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', )


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'username', 'user_image', 'first_name', 'last_name', )
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'user_image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
