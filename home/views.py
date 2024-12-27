from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from pyexpat.errors import messages

from .forms import LoginForm, SignUpForm


def home(request):
    return render(request, 'base.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("girdi")
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')  # Kullanıcıyı ana sayfaya yönlendirin
            else:
                form.add_error(None, 'Invalid email or password')  # Hatalı giriş
        else:
            # Eğer form geçerli değilse, burada form hatalarını kontrol edebilirsiniz
            print(form.errors)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)  # Kullanıcıyı çıkart
    return redirect('login')  # Giriş sayfasına yönlendir


CustomUser = get_user_model()

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Form verilerini alıyoruz
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # CustomUser modelini kullanarak kullanıcıyı kaydediyoruz
            user = CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Başarılı mesaj
            return HttpResponse("Kayıt başarılı! Giriş yapabilirsiniz.")
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})