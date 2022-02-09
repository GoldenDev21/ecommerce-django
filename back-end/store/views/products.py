from store.serializers import ProductSerializer, VariantSerializer
from store.models import Product, Variant
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# PRODUCTS

@api_view(['GET'])
@permission_classes([AllowAny])
def products_list_view(request):
    """
    View that returns a list of all products.

    Accessible by all.
    """
    serializer = ProductSerializer(Product.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def product_edit_delete_view(request, pk):
    """
    View that allows the update or deletion of a single product.

    Accessible only by admin.
    """
    try:
        product = Product.objects.get(pk=pk)
    except product.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def product_create_view(request):
    """
    Allows the creation of a single product or lists all products.

    Accessible only by admin.
    :param request:
    :return:
    """
    if request.method == 'GET':
        serializer = ProductSerializer(Product.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# VARIANTS


@api_view(['GET'])
@permission_classes([AllowAny])
def variant_list_view(request):
    """
    View that returns a list of all variants.

    Accessible by all.
    """
    serializer = VariantSerializer(Variant.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def variant_edit_delete_view(request, pk):
    """
    View that allows the update or deletion of a single variant.

    Accessible only by admin.
    """
    try:
        variant = Variant.objects.get(pk=pk)
    except variant.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(variant)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(variant, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        variant.delete()
        return Response(status=204)



