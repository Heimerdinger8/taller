from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Mechanic, ServiceOrder, SparePart
from .forms import SparePartForm

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


class ServiceOrderPaymentUpdateView(UpdateView):
    model = ServiceOrder
    fields = ['budget', 'down_payment']
    success_url = reverse_lazy('historial')

    def form_valid(self, form):
        # Ensure that the remaining payment is recalculated upon update
        instance = form.save(commit=False)
        if instance.budget is not None and instance.down_payment is not None:
            instance.remaining_payment = instance.budget - instance.down_payment
        else:
            instance.remaining_payment = 0
        instance.save()
        return super().form_valid(form)


class SparePartListView(ListView):
    model = SparePart
    template_name = 'inventory.html'
    context_object_name = 'spareparts'


class SparePartCreateView(CreateView):
    model = SparePart
    template_name = 'catalogs/sparepart_form.html'
    form_class = SparePartForm
    success_url = reverse_lazy('inventory')


class SparePartUpdateView(UpdateView):
    model = SparePart
    template_name = 'catalogs/sparepart_form.html'
    form_class = SparePartForm
    success_url = reverse_lazy('inventory')


class SparePartDeleteView(DeleteView):
    model = SparePart
    template_name = 'catalogs/sparepart_confirm_delete.html'
    success_url = reverse_lazy('inventory')
