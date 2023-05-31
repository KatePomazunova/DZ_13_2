from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseServerError
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

def user_signup(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='quotes:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})
   

def user_login(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:main')
      
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})


def user_logout(request):
    logout(request)
    return redirect(to='quotes:main')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'