from rest_framework import serializers
from .models import *

class ProdutoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco_unitario']


class QuartoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    hospede_atual = serializers.SerializerMethodField()

    class Meta:
        model = Quarto
        fields = ['id', 'diaria', 'hospede_atual', 'hospede_ativo']

    def get_hospede_atual(self, obj):
        return obj.hospede_atual.nome_completo if obj.hospede_atual else None



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
    
    hospede = serializers.SerializerMethodField()

    class Meta:
        model = Reserva
        fields = '__all__'

    def get_hospede(self, obj):
        return obj.hospede.nome_completo

class EstoqueSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    data_registro = serializers.DateTimeField(read_only=True)
    data_ultima_atualizacao = serializers.DateTimeField(read_only=True)

    produto = serializers.SerializerMethodField()
    
    class Meta:
        model = Estoque
        fields = '__all__'
    
    def get_produto(self, obj):
        return obj.produto.nome


class ConsumoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    data_registro = serializers.DateTimeField(read_only=True)
    data_ultima_atualizacao = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Consumo
        fields = '__all__'