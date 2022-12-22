from django.urls import path
from AppUno.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
]