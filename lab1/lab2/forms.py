from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, EmailValidator, MinLengthValidator
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    # Добавляем требования к username
    username = forms.CharField(
        label="Username",
        max_length=256,
        min_length=7,
        required=True,
        help_text="Минимальная длина 7 символов",
        validators=[
            RegexValidator(
                regex=re.compile(r'^[A-Z][a-zA-Z]+$'),
                message="1. Содержит только буквы латинского алфавита. 2. Начинается с большой буквы.",
                code='invalid_username'
            ),
        ],
    )

    # Добавляем требования к email
    email = forms.EmailField(
        label="Email",
        min_length=5,
        max_length=254,
        required=True,
        help_text="Email некорректный.",
        validators=[
            EmailValidator(message="Email некорректный.", code='invalid_email'),
        ],
    )

    # Добавляем требования к password
    password1 = forms.CharField(
        label="Password",
        strip=False,
        max_length=256,
        min_length=8,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text="1. Минимальная длина 8 символов.",
        validators=[
            RegexValidator(
                regex=re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])'),
                message="2. Содержит не менее 1 цифры. 3. Содержит не менее 1 символа. 4. Содержит не менее чем по 1 символу в верхнем и нижнем регистре.",
                code='invalid_password',
            ),
        ],
    )

    # Добавляем требования к birthday
    birthday = forms.DateField(
        label="Birthday",
        input_formats=['%Y-%m-%d'],
        help_text="Формат YYYY-MM-DD.",
    )

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'birthday')

