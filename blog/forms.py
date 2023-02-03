from dataclasses import fields
from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'type': "text",
                                                         'class': "form-control",
                                                         'id': "name",
                                                         }))
    email = forms.CharField(label='Ваш email',widget=forms.EmailInput(attrs={'type': "email",
                                                           'class': "form-control",
                                                           'id': "email",
                                                           }))
    description = forms.CharField(label='Комментарий',widget=forms.Textarea(attrs={'id': "message", 
                                                               'cols': 30,
                                                               'rows': 5,
                                                               'class': "form-control",
                                                           }))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'description']