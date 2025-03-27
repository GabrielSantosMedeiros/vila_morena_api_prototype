from rest_framework import serializers
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco_unitario']


class QuartoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Quarto
        fields = ['id', 'diaria', 'hospede_atual', 'hospede_ativo']



class HospedeSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    data_registro = serializers.DateTimeField(read_only=True)
    data_ultima_atualizacao = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Hospede
        fields = ['id', 'nome_completo', 'documento', 'tipo_documento', 'data_nascimento', 'data_registro', 'data_ultima_atualizacao'] 


class ReservaSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    data_registro = serializers.DateTimeField(read_only=True)
    data_ultima_atualizacao = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = Reserva
        fields = '__all__'