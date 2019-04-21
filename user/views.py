from django.views.generic.base import View

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from user.auth_backends import authenticate

from user.forms import ProfileRegisterForm, LoginForm


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
        pass


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=user_email, password=password)
            if user:
                login(request, user)
                return redirect('index')
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        profile_form = ProfileRegisterForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/user/login/')
        return render(request, 'register.html', {'profile_form': profile_form})
    else:
        profile_form = ProfileRegisterForm()
        return render(request, 'register.html', {'profile_form': profile_form})