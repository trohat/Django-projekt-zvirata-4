from django.urls import path
from . import views

urlpatterns = [
    path("zirafa/", views.zirafa),
    path("<int:zvire>/", views.cislo),
    path("<str:zvire>/", views.o_zvireti),
    path("<kategorie>/<druh>/", views.taxonomie),
    path("", views.o_zviratech)
]

