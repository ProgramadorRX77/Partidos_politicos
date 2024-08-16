from django.urls import path
from .views import lista_partidos
from . import views

"""urlpatterns = [
    path('partidos/', lista_partidos, name='lista_partidos'),
]"""



urlpatterns = [
    path('api/partidos/', views.lista_partidos, name='lista_partidos'),
    path('app1/', views.lista_partidos, name="partidos"),
]
