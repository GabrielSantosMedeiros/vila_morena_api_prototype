from django.shortcuts import render
from rest_framework import viewsets 
from .models import *
from .serializers import *

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset=Produto.objects.all()
    serializer_class=ProdutoSerializer

    Produto._result_cache = None


class QuartoViewSet(viewsets.ModelViewSet):
    queryset=Quarto.objects.all()
    serializer_class=QuartoSerializer

    Quarto._result_cache = None


class HospedeViewSet(viewsets.ModelViewSet):
    queryset=Hospede.objects.all()
    serializer_class=HospedeSerializer

    Hospede._result_cache = None


class ReservaViewSet(viewsets.ModelViewSet):
    queryset=Reserva.objects.all()
    serializer_class=ReservaSerializer

    Reserva._result_cache = None


class EstoqueViewSet(viewsets.ModelViewSet):
    queryset=Estoque.objects.all()
    serializer_class=EstoqueSerializer


class ConsumoViewSet(viewsets.ModelViewSet):
    queryset=Consumo.objects.all()
    serializer_class=ConsumoSerializer