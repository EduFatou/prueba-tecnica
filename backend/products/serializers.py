from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, help_text="ID único del producto")
    name = serializers.CharField(max_length=100, help_text="Nombre del producto")
    price = serializers.DecimalField(max_digits=6, decimal_places=2, help_text="Precio del producto en euros")

    class Meta:
        example = {
            "id": 1,
            "name": "Portátil",
            "price": 600.00
        }