from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def slon(request):
    return HttpResponse("SLOOOOOOOOON troubí")

def zirafa(request):
    return HttpResponse("<h1>Žirafa má dlouhý krk</h1>")

def o_zviratech(request):
    return HttpResponse("<p>Máme rádi zvířata</p>")

