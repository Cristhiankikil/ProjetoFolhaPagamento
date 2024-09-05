from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
    
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    endereco = models.CharField(max_length=20)
    setor = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Cargo(models.Model):
    nome = models.CharField(max_length=30)
    salarioBase = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)
    beneficio = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Beneficio(models.Model):
    nome = models.CharField(max_length=30)
    valor = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    
class Folha_de_pagamento (models.Model):
    data = models.DateField()
    valorLiquido = models.FloatField(max_length=8)
    valorBruto = models.FloatField(max_length=8)
    horaExtra = models.FloatField(max_length=6)
    horasTrabalhadas = models.FloatField(max_length=4)
    adicionalNoturno = models.FloatField(max_length=4)
    adicionalInsalubridade = models.FloatField(max_length=6)
    
class Funcionario (models.Model):
    nome = models.CharField(max_length=50)
    salarioBase = models.FloatField(max_length=8)
    nivel = models.IntegerField(max_length=1)
    def __str__(self):
        return self.nome
    