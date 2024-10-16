from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProductList(APIView):
    @swagger_auto_schema(
        operation_description="Obtiene la lista de todos los productos disponibles",
        responses={
            200: openapi.Response(
                description="Lista de productos recuperada con éxito",
                schema=ProductSerializer(many=True)
            )
        },
        tags=['productos']
    )
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

    @swagger_auto_schema(
        operation_description="Crea un nuevo producto (simulado)",
        request_body=ProductSerializer,
        responses={
            201: openapi.Response(
                description="Producto creado con éxito",
                schema=ProductSerializer
            ),
            400: openapi.Response(
                description="Datos de entrada inválidos",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        },
        tags=['productos']
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=201)
        return Response({"error": "Datos de entrada inválidos"}, status=400)