from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todos.models import *

class TodoListView(ListView):
    model = Empresas  

class TodoCreateView(CreateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("listar")

class TodoUpdateView(UpdateView):
    model = Empresas
    fields = ["id","nome","email", "senha", "jogo", "logo", "desc"]
    success_url = reverse_lazy("listar")

class TodoDeleteView(DeleteView):
    model = Empresas
    success_url = reverse_lazy("listar")
