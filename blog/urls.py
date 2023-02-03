from django.urls import path
from .views import *


urlpatterns = [
    path('blog/', PostList.as_view(), name='blog'),
    path('blog/<slug:slug>', PostDetail.as_view(), name='post_detail'),

]