from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator, EmailValidator

class Mechanic(models.Model):
    name = models.CharField("Nombre", max_length=100, validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Name can only contain letters and spaces.')])
    phone_regex = RegexValidator(regex=r'^\\d{10}$', message="El número de teléfono debe tener 10 dígitos.")
    phone = models.CharField("Teléfono", validators=[phone_regex], max_length=10, blank=True, null=True)
    email = models.EmailField("Correo Electrónico", blank=True, null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Name can only contain letters and spaces.')])
    address = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\\d{10}$', message="El número de teléfono debe tener 10 dígitos.")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    whatsapp = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)
    email = models.EmailField(max_length=254, validators=[EmailValidator(message='Enter a valid email address.')]) # Standard max length for email
    receive_promotions = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ServiceOrder(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    date = models.DateField()
    time = models.TimeField()
    vehicle_brand = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=30)
    vehicle_serial_number = models.CharField(max_length=50, unique=True)
    vehicle_motor_number = models.CharField(max_length=50, unique=True)
    vehicle_plates = models.CharField(max_length=10, unique=True)
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    departure_date = models.DateField()
    departure_time = models.TimeField()
    mileage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    GAS_LEVEL_CHOICES = [
        ('Empty', 'Empty'),
        ('1/4', '1/4'),
        ('1/2', '1/2'),
        ('3/4', '3/4'),
        ('Full', 'Full'),
    ]
    STATUS_CHOICES = [
        ('Good', 'Good'),
        ('Regular', 'Regular'),
        ('Bad', 'Bad'),
    ]
    gas_level = models.CharField(max_length=20, choices=GAS_LEVEL_CHOICES)
    main_failure = models.TextField(max_length=500)
    engine_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    electrical_system_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    brakes_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    suspension_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    fluid_level_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tires_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tuning_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    other_details = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='service_orders/', blank=True, null=True)
    warranty_included = models.BooleanField(default=False)
    warranty_valid_from = models.DateField(blank=True, null=True)
    warranty_valid_to = models.DateField(blank=True, null=True)
    warranty_exception = models.CharField(max_length=200, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    down_payment = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=True)

    def save(self, *args, **kwargs):
        self.remaining_payment = self.budget - self.down_payment
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_number} - {self.client.name}"

class InventoryItem(models.Model):
    service_order = models.ForeignKey(ServiceOrder, related_name='inventory_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    has_item = models.BooleanField()
    specification = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class SparePart(models.Model):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", blank=True, null=True)
    quantity = models.PositiveIntegerField("Cantidad", default=0)
    price = models.DecimalField("Costo Unitario", max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField("Imagen", upload_to='spare_parts/', blank=True, null=True)

    @property
    def total_cost(self):
        return self.quantity * self.price

    def __str__(self):
        return self.name