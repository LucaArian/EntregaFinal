from django.urls import path
from AppUno.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('primos/', primos, name="primos"),
    path('padres/', padres, name="padres"),
    path('abuelos/', abuelos, name="abuelos"),
    path("abueloFormulario/", abueloFormulario, name="abueloFormulario"),
    path("primoFormulario/", primoFormulario, name="primoFormulario"),
    path("padreFormulario", padreFormulario, name="padreFormulario"),
    path("busquedaNombre/", busquedaNombre, name="busquedaNombre"),
    path("buscar/", buscar, name="buscar"),

]