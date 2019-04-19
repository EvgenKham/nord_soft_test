from django.urls import re_path
from user.views import login_view, register_view, LogoutView


urlpatterns = [
    re_path(r'^register/$', register_view, name='register'),
    re_path(r'^login/$', login_view, name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
]