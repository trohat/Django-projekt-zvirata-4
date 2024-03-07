from django.urls import path
from . import views

urlpatterns = [
    # path("zirafa/", views.zirafa, name="zirafa"),
    path("seznam/", views.seznam, name="seznam_zvirat"),
    # path("<int:zvire>/", views.cislo),
    path("<int:id>/", views.o_zvireti, name="zvire"),
    # path("<kategorie>/<druh>/", views.taxonomie),
    path("", views.o_zviratech, name="o_zviratech")
]

