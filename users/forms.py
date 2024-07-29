from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'username', 'user_image', 'first_name', 'last_name',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'user_image': forms.FileInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserProfileForm(forms.ModelForm):
    email = forms.CharField(disabled=True, label='Электронная почта',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(disabled=True, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(disabled=True, label='Статус пользователя',
                                   widget=forms.CheckboxInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'user_image', 'is_active')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'user_image': 'Аватар',
            'is_active': 'Статус',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
