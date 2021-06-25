from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pozycja, Postac, Rola






def index(request):
    wszystkie = Postac.objects.all()

    dane = {'kategorie': wszystkie}

    return render(request, 'szablon1.html', dane)
