from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todos.models import *

# CRUD PARA A EMPRESA

class TodoListView(ListView):
    model = Empresas

class TodoCreateView(CreateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("listarEmpresas")

class TodoUpdateView(UpdateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("listarEmpresas")

class TodoDeleteView(DeleteView):
    model = Empresas
    success_url = reverse_lazy("listarEmpresas")

# CRUD PARA JOGO

class Selctjogo(ListView):
    model = jogo

class InsertJogos(CreateView):
    model = jogo
    fields = ["id","empresa","nome", "preco", "desc", "foto", "data_lancamento"]
    success_url = reverse_lazy("listarJogo")

class UpdateJogo(UpdateView):
    model = jogo
    fields = ["id","empresa","nome", "preco", "desc", "foto", "data_lancamento"]
    success_url = reverse_lazy("listarJogo")
    
class DeleteJogo(DeleteView):
    model = jogo
    success_url = reverse_lazy("listarJogo")