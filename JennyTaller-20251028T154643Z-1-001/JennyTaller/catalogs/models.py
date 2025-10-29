from django.db import models

class Mechanic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField()
    receive_promotions = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ServiceOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    vehicle_brand = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=30)
    vehicle_serial_number = models.CharField(max_length=50)
    vehicle_motor_number = models.CharField(max_length=50)
    vehicle_plates = models.CharField(max_length=10)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    departure_date = models.DateField()
    departure_time = models.TimeField()
    mileage = models.IntegerField()
    gas_level = models.CharField(max_length=20)
    main_failure = models.TextField()
    engine_status = models.CharField(max_length=20)
    electrical_system_status = models.CharField(max_length=20)
    brakes_status = models.CharField(max_length=20)
    suspension_status = models.CharField(max_length=20)
    fluid_level_status = models.CharField(max_length=20)
    tires_status = models.CharField(max_length=20)
    tuning_status = models.CharField(max_length=20)
    other_details = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='service_orders/', blank=True, null=True)
    warranty_included = models.BooleanField(default=False)
    warranty_valid_from = models.DateField(blank=True, null=True)
    warranty_valid_to = models.DateField(blank=True, null=True)
    warranty_exception = models.CharField(max_length=200, blank=True, null=True)
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_number} - {self.client.name}"

class InventoryItem(models.Model):
    service_order = models.ForeignKey(ServiceOrder, related_name='inventory_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    has_item = models.BooleanField()
    specification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name