from django.urls import path
from .views import lista_partidos

urlpatterns = [
    path('partidos/', lista_partidos, name='lista_partidos'),
]
