from django import forms
from .models import Message, User
from django.contrib.auth.forms import UserCreationForm

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields="__all__"
        exclude=['user','post']

class MyUserCreationForm(UserCreationForm):
    last_name = forms.CharField(label='Ism', max_length=100)
    first_name = forms.CharField(label='Familya', max_length=100)
    email = forms.CharField(label='Email manzil',widget=forms.EmailInput)
    password1 = forms.CharField(label='Parol',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni qayta kiriting',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['last_name', 'first_name',  'email', 'password1', 'password2']
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Parollar mos emas.')
        return cd['password2']
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'last_name', 'first_name', 'email']