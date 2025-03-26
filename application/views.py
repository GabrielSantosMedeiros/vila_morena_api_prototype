from django.shortcuts import render
from rest_framework import viewsets 
from .models import Produto
from .serializers import ProdutoSerializer

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset=Produto.objects.all()
    serializer_class=ProdutoSerializer
    