from django.urls import path
from . import views

urlpatterns = [
    path("zirafa/", views.zirafa),
    path("<zvire>/", views.o_zvireti),
    path("", views.o_zviratech)
]

