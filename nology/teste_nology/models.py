from django.db import models

# Create your models here.
class Compra(models.Model):
    tipo_cliente = models.CharField(max_length=20, null=False, choices=[
        ('comum', 'Comum'),
        ('vip', 'VIP'),
    ])
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cashback = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ip_cliente = models.GenericIPAddressField(null=True, blank=True)
