
from django import forms 

from .models import Pavilon, Zvire


class ZvireForm(forms.Form):
    jmeno = forms.CharField(max_length=30, label="Zadej jméno:", required=True)
    druh = forms.CharField(max_length=30)
    vek = forms.IntegerField(label="věk", required=False)
    popis = forms.CharField(max_length=200)
    pavilon = forms.ModelChoiceField(queryset=Pavilon.objects.all(), empty_label="(Žádný pavilon)")