from django import forms
from captcha.fields import CaptchaField
from .models import *

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'type': "text",
                                                         'class': "form-control", 
                                                         'id': "name",
                                                         'required': "required",}))
    email = forms.CharField(label='Ваш email', widget=forms.EmailInput(attrs={'type': "email",
                                                         'class': "form-control", 
                                                         'id': "email",
                                                         'required': "required",}))
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea(attrs={'class': "form-control", 
                                                         'rows': 8,
                                                         'id': "message",
                                                         'required': "required",}))
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)