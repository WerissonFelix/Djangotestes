
from django.views.generic import ListView, CreateView
from  todos.models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo
   

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"] # o que o usuário vai add no db
    success_url = reverse_lazy("todo_list") # para onde a view irá dps da adição
    