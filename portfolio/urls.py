from django.urls import path
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='portfolio/index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='portfolio/about.html'), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),

]