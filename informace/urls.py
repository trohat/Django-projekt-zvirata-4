from django.urls import path
from . import views

urlpatterns = [
    path("slon/", views.slon),
    path("zirafa/", views.zirafa),
    path("", views.o_zviratech)
]

