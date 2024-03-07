from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

from .models import Zvire

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
        if zvire in diakritika:
            zvire = diakritika[zvire]
     
        return render(request, "informace/zvire.html", {
            "popis": popis,
            "jmeno_zvirete": zvire
        })
    else:
        return HttpResponseNotFound(f"{zvire} není v naší zoo.")

def seznam(request):
    zvirata = Zvire.objects.all()
    return render(request, "informace/seznam.html", {
        "seznam": zvirata
    })

def zirafa(request):
    # load template
    # create template    
    # load context  
    # return template with context
    # create HttpResponse
    min_pocet_pro_akci = 10
    seznam = ["a", "b"]
    chybi_do_deseti = min_pocet_pro_akci - len(seznam)
    return render(request, "informace/zirafa.html", {
        "delka_krku": 3,
        "seznam_ziraf": seznam,
        "chybi": chybi_do_deseti
    })

def o_zviratech(request):
    return render(request, "informace/o_zviratech.html", {
        "zvire1": "orangutan",
        "zvire2": "gORILA",
        "mysi": 3,
        "otevreny_pavilon": None,
        "datum": datetime.now()
    })

def index(request):
    sef = "Lukáš Chovatel-tygrů"
    pocet_zvirat = 253
    return render(request, "informace/uvod.html", {
        "sef": sef,
        "pocet": pocet_zvirat
    })

def cislo(request, zvire):
    return HttpResponse(f"<h2>Číslo zvířete je {zvire}</h2>")

def taxonomie(request, kategorie, druh):
    return HttpResponse(f"<p>Kategorie je {kategorie}.</p><p>Druh je {druh}.</p>")