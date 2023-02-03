from django.shortcuts import render
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect


class ContactFormView(CreateView):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('contact')