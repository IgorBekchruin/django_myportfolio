from email import message
from operator import mod
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'