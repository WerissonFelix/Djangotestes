from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name= "titulo",max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    deadline = models.DateTimeField(verbose_name="data de entrega",null=False, blank=False)
    finished_at = models.DateTimeField(null=True)


class alunos(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    ano = models.DateTimeField(auto_now=True, null=False, blank=False)
    idade = models.DateTimeField(null=False, blank=False)
    matricula = models.DateTimeField(null=True)
