from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from user.models import Profile


class ProfileRegisterForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email', 'first_name', 'last_name', 'number_phone', 'city', 'address']
        labels = {
            'email': 'Email',
            'first_name': 'First name',
            'last_name': 'Last name',
            'number_phone': 'Number phone',
            'city': 'City',
            'address': 'Address'
        }
        help_texts = {
            'email': 'Specify real mail'
        }

    def clean(self):
        email = self.cleaned_data['email']

        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с данной почтой уже зарегистрирован')

    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.password = profile.generation_password()
        if commit:
            profile.save()

        return profile


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Эл. почта'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        user_email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not Profile.objects.filter(email=user_email).exists():
            raise forms.ValidationError('Пользователя с данной почтой НЕ существует!')

        # profile = Profile.objects.get(email=user_email)
        # if profile and not check_password(password):
        #     raise forms.ValidationError('Неверный пароль. Попробуйте снова')