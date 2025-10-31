from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Mechanic

class ClientListView(ListView):
    model = Client
    template_name = 'catalogs/client_list.html'
    context_object_name = 'clients'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'catalogs/client_form.html'
    fields = '__all__'
    success_url = reverse_lazy('catalogs:client_list')

class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'catalogs/client_form.html'
    fields = '__all__'
    success_url = reverse_lazy('catalogs:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'catalogs/client_confirm_delete.html'
    success_url = reverse_lazy('catalogs:client_list')

class MechanicCreateView(CreateView):
    model = Mechanic
    template_name = 'catalogs/mechanic_form.html'
    fields = '__all__'
    success_url = reverse_lazy('catalogs:mechanic_list')

class MechanicListView(ListView):
    model = Mechanic
    template_name = 'catalogs/mechanic_list.html'
    context_object_name = 'mechanics'

class MechanicUpdateView(UpdateView):

    model = Mechanic

    template_name = 'catalogs/mechanic_form.html'

    fields = '__all__'

    success_url = reverse_lazy('catalogs:mechanic_list')



class MechanicDeleteView(DeleteView):

    model = Mechanic

    template_name = 'catalogs/mechanic_confirm_delete.html'

    success_url = reverse_lazy('catalogs:mechanic_list')
