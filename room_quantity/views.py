from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from configs.response import getResponse, createResponse, errorResponse, notFoundResponse, updateResponse, \
    deleteResponse
from room_quantity.models import RoomQuantity
from room_quantity.seriailizer import RoomQuantitySerializer, RoomQuantityDetailSerializer


# Create your views here.

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @user_is_admin_or_super_admin
def get_or_create(request):
    if request.method == "GET":
        hotel = RoomQuantity.objects.filter(is_deleted=False).all()
        serializer = RoomQuantitySerializer(hotel, many=True)
        return getResponse(serializer.data)

    if request.method == "POST":
        serializer = RoomQuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return createResponse(serializer.data)
        return errorResponse(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @user_is_admin_or_super_admin
def get_or_update_or_delete(request, pk):
    try:
        hotel = RoomQuantity.objects.filter(is_deleted=False).get(pk=pk)
    except:
        return notFoundResponse()

    if request.method == "GET":
        serializer = RoomQuantityDetailSerializer(hotel)
        return getResponse(serializer.data)

    if request.method == "PUT":
        serializer = RoomQuantitySerializer(hotel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return updateResponse(serializer.data)
        return errorResponse(serializer.errors)

    if request.method == 'DELETE':
        serializer = RoomQuantitySerializer(hotel, data={"is_deleted": True}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return deleteResponse()
        return errorResponse(serializer.errors)
