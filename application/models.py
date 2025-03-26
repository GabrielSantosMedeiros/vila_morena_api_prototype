from django.db import models
from django.utils import timezone

# Create your models here.
class Hospede(models.Model):
    id = models.UUIDField(primary_key=True)
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
    id = models.UUIDField(primary_key=True)
    hospede = models.ForeignKey(to=Hospede, on_delete=models.CASCADE, null=False, blank=False)
    quarto = models.ForeignKey(to=Quarto, on_delete=models.CASCADE, null=False, blank=False)
    data_inicio = models.DateField(null=False, blank=False)
    data_fim = models.DateField(null=False, blank=False)
    check_in = models.BooleanField(default=False)
    data_registro = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reservas'
    
