from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

slovnik = {
    "opice": "Opice má palce podobné jako člověk.",
    "pes": "Pes je přítel člověka.",
    "kocka": "Šelma a zároveň mazlíček.",
    "kralik": "Králík ma dlouhé uši.",
    "tucnak": "Rád skáče do vody a plave.",
    "slon": "Slon troubí hodně nahlas."
}

diakritika = {
    "kocka": "kočka",
    "kralik": "králík",
    "tucnak": "tučňák"
}

def o_zvireti(request, zvire):
    print(f"Přišel mi parametr {zvire}")
    if zvire in slovnik:
        popis = slovnik[zvire]
        odpoved = ""
        if zvire in diakritika:
            odpoved += f"<h1>{diakritika[zvire].capitalize()}</h1>"
        else:
            odpoved += f"<h1>{zvire.capitalize()}</h1>"
        odpoved += f"<p>{popis}</p>"
        print(odpoved)
        return HttpResponse(odpoved)
    else:
        return HttpResponseNotFound(f"{zvire} není v naší zoo.")

def zirafa(request):
    return HttpResponse("<h1>Žirafa má dlouhý krk</h1>")

def o_zviratech(request):
    return HttpResponse("<p>Máme rádi zvířata</p>")

def index(request):
    return HttpResponse("<h2>Vítejte v naší aplikaci o zvířatech</h2>")