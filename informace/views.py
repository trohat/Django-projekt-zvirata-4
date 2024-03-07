from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound
from datetime import datetime

from .models import Zvire

# Create your views here.

def o_zvireti(request, id):
    # try:
    #     zvire = Zvire.objects.get(pk=id)
    # except:
    #     return Http404()
    zvire = get_object_or_404(Zvire, pk=id)

    popis = zvire.popis.rstrip(".")
    return render(request, "informace/zvire.html", {
        "zvire": zvire,
        "nadpis": f"{zvire.druh.lower()} {zvire.jmeno.title()}",
        "popis": popis
    })

def seznam(request):
    zvirata = Zvire.objects.all()
    return render(request, "informace/seznam.html", {
        "seznam": zvirata
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

"""
starý kód, na něm jsme se učili routování a filtry v šablonách
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

def cislo(request, zvire):
    return HttpResponse(f"<h2>Číslo zvířete je {zvire}</h2>")

def taxonomie(request, kategorie, druh):
    return HttpResponse(f"<p>Kategorie je {kategorie}.</p><p>Druh je {druh}.</p>")
"""