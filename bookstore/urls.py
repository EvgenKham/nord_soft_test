from django.urls import path, re_path
from bookstore.views import *

urlpatterns = [
    path('', index, name='index'),
    ]