from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Pozycja, Postac, Rola

import cassiopeia as cass




def index(request):
    wszystkie = Postac.objects.all()
    test = cass.get_champions()
    dane = {'kategorie': wszystkie}

    return render(request, 'szablon1.html', test)
