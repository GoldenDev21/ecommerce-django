from store.serializers import CategorySerializer
from store.models import Category
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


@api_view(['GET'])
@permission_classes([AllowAny])
def categories_list_view(request):
    """
    View that returns a list of all categories.

    Accessible by all.
    """
    serializer = CategorySerializer(Category.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def category_edit_delete_view(request, pk):
    """
    View that allows the update or deletion of a single category.

    Accessible only by admin.
    """
    try:
        category = Category.objects.get(pk=pk)
    except category.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def category_create_view(request):
    """
    Allows the creation of a single category or lists all categories.

    Accessible only by admin.
    :param request:
    :return:
    """
    if request.method == 'GET':
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
