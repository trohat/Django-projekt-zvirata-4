from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from datetime import datetime

from .models import Zvire
from .forms import ZvireForm

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

def pridej(request):
    if request.method == "POST":
        formular = ZvireForm(request.POST)
        if formular.is_valid():
            #zde dochází ke zpracování dat
            zvire = Zvire(jmeno=formular.cleaned_data["jmeno"],
                        druh=formular.cleaned_data["druh"],
                        vek=formular.cleaned_data["vek"],
                        popis=formular.cleaned_data["popis"],
                        pavilon=formular.cleaned_data["pavilon"]
                            )
            zvire.save()
            return HttpResponseRedirect(reverse("dekuji"))
    else:
        formular = ZvireForm()
    return render(request, "informace/pridani.html", {
        "formular": formular
    })

def dekuji(request):
    return render(request, "informace/dekuji.html")

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