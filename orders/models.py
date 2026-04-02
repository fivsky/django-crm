from django.db import models
from decimal import Decimal


class Product(models.Model):
    MATERIAL_CHOICES = [
        ('SBR', 'SBR'),
        ('SBR+EPDM', 'SBR+EPDM'),
    ]
    name = models.CharField(max_length=100, default="Резиновая плитка")
    thickness = models.PositiveSmallIntegerField(
        choices=[(20,'20 мм'),(25,'25 мм'),(30,'30 мм'),(35,'35 мм'),(40,'40 мм')]
    )
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    price_per_m2 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_material_display()} {self.thickness}мм"

class Client(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # количество плиток
    order_date = models.DateTimeField(auto_now_add=True)

def total_price(self):
    area = self.quantity * Decimal('0.25')
    return area * self.product.price_per_m2

    def __str__(self):
        return f"Заказ #{self.id} от {self.client.name}"