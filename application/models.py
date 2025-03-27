from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Hospede(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nome_completo = models.CharField(max_length=255, null=False, blank=False)
    documento = models.CharField(max_length=20, null=False, blank=False)
    tipo_documento = models.CharField(max_length=20, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'hospedes'



class Quarto(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    diaria = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    hospede_atual = models.OneToOneField(to=Hospede, on_delete=models.SET_NULL, null=True, blank=True)
    hospede_ativo = models.BooleanField(default=False)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'quartos'


class Reserva(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    hospede = models.ForeignKey(to=Hospede, on_delete=models.CASCADE, null=False, blank=False)
    quarto = models.ForeignKey(to=Quarto, on_delete=models.CASCADE, null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=False, blank=False)
    check_in = models.BooleanField(default=False)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reservas'



class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=128, unique=True)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'produtos'



class Estoque(models.Model):
    id = models.IntegerField(primary_key=True)
    produto = models.ForeignKey(to=Produto, on_delete=models.CASCADE, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'estoque'



class Consumo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reserva = models.ForeignKey(to=Reserva, on_delete=models.SET_NULL, null=True, blank=True)
    produto = models.ForeignKey(to=Produto, on_delete=models.CASCADE, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'consumo'
