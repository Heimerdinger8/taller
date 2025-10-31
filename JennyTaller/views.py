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

    def post(self, request, *args, **kwargs):
        client_email = request.POST.get('correo')
        client, created = Client.objects.get_or_create(
            email=client_email,
            defaults={
                'name': request.POST.get('nombre'),
                'address': request.POST.get('domicilio'),
                'phone': request.POST.get('telefono'),
                'whatsapp': request.POST.get('whatsapp'),
                'receive_promotions': False,  # O manejarlo desde el form
            }
        )

        mechanic_id = request.POST.get('mechanic')
        mechanic = Mechanic.objects.get(id=mechanic_id)

        service_order = ServiceOrder.objects.create(
            client=client,
            mechanic=mechanic,
            date=request.POST.get('fecha'),
            time=request.POST.get('hora'),
            vehicle_brand=request.POST.get('marca'),
            vehicle_model=request.POST.get('modelo'),
            vehicle_color=request.POST.get('color'),
            vehicle_serial_number=request.POST.get('no_serie'),
            vehicle_motor_number=request.POST.get('no_motor'),
            vehicle_plates=request.POST.get('placa'),
            # Assuming arrival and departure are not in the form yet
            arrival_date=request.POST.get('fecha'), # Placeholder
            arrival_time=request.POST.get('hora'), # Placeholder
            departure_date=request.POST.get('fecha'), # Placeholder
            departure_time=request.POST.get('hora'), # Placeholder
            mileage=request.POST.get('kilometraje'),
            gas_level=request.POST.get('gasolina'),
            main_failure=request.POST.get('falla_principal'),
            engine_status=request.POST.get('motor'),
            electrical_system_status=request.POST.get('electrico'),
            brakes_status=request.POST.get('frenos'),
            suspension_status=request.POST.get('suspension'),
            fluid_level_status=request.POST.get('liquidos'),
            tires_status=request.POST.get('llantas'),
            tuning_status=request.POST.get('afinacion'),
            other_details=request.POST.get('otros'),
            warranty_included=request.POST.get('garantia') == 'si',
            warranty_valid_from=request.POST.get('valida_desde'),
            warranty_valid_to=request.POST.get('valida_hasta'),
            warranty_exception=request.POST.get('excepcion'),
            down_payment=request.POST.get('anticipo'),
            remaining_payment=request.POST.get('restan'),
        )
        service_order.order_number = service_order.id
        service_order.save()
        return redirect('search')
