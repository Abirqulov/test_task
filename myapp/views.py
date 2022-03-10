from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CreateUserForm
from .models import Contact, Contact_Post, New
import requests
from rest_framework import generics
from django.contrib import messages
# Create your views here.
import json


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Accaunt was created for ' + user)

            return redirect('login')
    else:
            form = CreateUserForm()
    return render(request, 'register.html', {'form':form})


def login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            print('log1', redirect('index'))
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def home(request):
    contact = Contact.objects.all()

    return render(request, 'index.html', {'contact': contact})


def about(request):
    contact = Contact.objects.all()
    return render(request, 'about.html', {'contact': contact})


def news(request):
    news = New.objects.all()

    if request.user.is_authenticated:
        print('user',  request.user)
        contact = Contact.objects.all()
        return render(request, 'course.html', {'contact': contact, 'news': news})
    else:
        print('user2 = ', request.user)
        return HttpResponseRedirect(reverse('login'))


def contact(request):
    contact = Contact.objects.all()

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        comment = request.POST["comment"]

        post = Contact_Post(name=name, email=email, subject=subject, comment=comment)
        post.save()

    return render(request, 'contact.html', {'contact': contact})


def json_response(request):
    response = requests.get('https://gorest.co.in/public/v1/posts?page=2')

    return render(request, 'json.html', {'response': response})


# with open('https://gorest.co.in/public/v1/posts') as json_file:
#     data = json.load(json_file)
#     print("type:", type(data))
#
#
# class Data(generics.ListAPIView):
#     queryset = data.objetcs.all()

