from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from catalogs.models import Mechanic, Client, ServiceOrder

def login_view(request):
    if request.method == 'POST':
        # Dummy authentication logic
        # In a real application, you would check credentials here
        return redirect('search')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def search_view(request):
    return render(request, 'search.html')

def inventory_view(request):
    return render(request, 'inventory.html')

class ServiceOrderView(View):
    def get(self, request, *args, **kwargs):
        mechanics = Mechanic.objects.all()
        clients = Client.objects.all()
        return render(request, 'service_order.html', {'mechanics': mechanics, 'clients': clients})
