import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_site01.settings')
django.setup()

from app1.models import PartidoPolitico

partidos = [
    {"nombre": "Partido Liberal", "fundacion": "1950-03-01", "lider": "Juan Pérez"},
    {"nombre": "Partido Conservador", "fundacion": "1960-06-15", "lider": "María Gómez"},
    {"nombre": "Partido Socialista", "fundacion": "1975-10-25", "lider": "Carlos Rodríguez"},
    {"nombre": "Partido Verde", "fundacion": "1980-08-30", "lider": "Ana López"},
]

for partido in partidos:
    PartidoPolitico.objects.create(**partido)

print("Datos de partidos políticos añadidos correctamente.")

