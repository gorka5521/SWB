from django.contrib import auth
from django.shortcuts import render, render_to_response
from django.template import loader

from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

from .models import Pozycja, Postac, Rola


def index(request):
    wszystkie = Postac.objects.all()

    dane = {'kategorie': wszystkie}

    return render(request, 'main.html', dane)

def login2(request):
    wszystkie = Postac.objects.all()

    dane = {'kategorie': wszystkie}

    return render(request, 'login.html', dane)

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('accounts/loggedin/')
    else:
        return HttpResponseRedirect('accounts/invalid/')

def loggedin(request):
    return render_to_response('loggedin.html',{'user_name' : request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def invalid_login(request):
    return render_to_response('invalid_login.html')

