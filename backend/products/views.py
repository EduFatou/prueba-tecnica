# products/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        products = [
            {'id': 1, 'name': 'Portátil', 'price': 600},
            {'id': 2, 'name': 'Teléfono', 'price': 450},
            {'id': 3, 'name': 'Auriculares', 'price': 90},
            {'id': 4, 'name': 'Teclado', 'price': 30},
            {'id': 5, 'name': 'Ratón', 'price': 25},
            {'id': 6, 'name': 'Monitor', 'price': 150},
            {'id': 7, 'name': 'Impresora', 'price': 200},
            {'id': 8, 'name': 'Tablet', 'price': 350}
        ]

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)