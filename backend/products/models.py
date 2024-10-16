from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Nombre del producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio del producto")

    def __str__(self):
        return self.name