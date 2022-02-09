from store.serializers import BrandSerializer
from store.models import Brand
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


@api_view(['GET'])
@permission_classes([AllowAny])
def brands_list_view(request):
    """
    View that returns a list of all brands.

    Accessible by all.
    """
    serializer = BrandSerializer(Brand.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def brand_edit_delete_view(request, pk):
    """
    View that allows the update or deletion of a single brand.

    Accessible only by admin.
    """
    try:
        brand = Brand.objects.get(pk=pk)
    except brand.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(brand, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        brand.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def brand_create_view(request):
    """
    Allows the creation of a single brand or lists all brands.

    Accessible only by admin.
    :param request:
    :return:
    """
    if request.method == 'GET':
        serializer = BrandSerializer(Brand.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BrandSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
