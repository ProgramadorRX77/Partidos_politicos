from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PartidoPolitico
from .serializers import PartidoPoliticoSerializer

def view_home(request):

    return render(request,"index.html")


@api_view(['GET'])
def lista_partidos(request):
    partidos = PartidoPolitico.objects.all()
    serializer = PartidoPoliticoSerializer(partidos, many=True)
    return Response(serializer.data)


