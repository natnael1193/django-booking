from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from configs.response import getResponse, createResponse, errorResponse, notFoundResponse, updateResponse, \
    deleteResponse
from room_type.models import RoomType
from room_type.serializer import RoomTypeSerializer, RoomTypeDetailSerializer


# Create your views here.

@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# @user_is_admin_or_super_admin
def get_or_create(request):
    if request.method == "GET":
        room_type = RoomType.objects.filter(is_deleted=False).all()
        serializer = RoomTypeSerializer(room_type, many=True)
        return getResponse(serializer.data)

    if request.method == "POST":
        serializer = RoomTypeSerializer(data=request.data)
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
        room_type = RoomType.objects.filter(is_deleted=False).get(pk=pk)
    except:
        return notFoundResponse()

    if request.method == "GET":
        serializer = RoomTypeDetailSerializer(room_type)
        return getResponse(serializer.data)

    if request.method == "PUT":
        serializer = RoomTypeSerializer(room_type, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return updateResponse(serializer.data)
        return errorResponse(serializer.errors)

    if request.method == 'DELETE':
        serializer = RoomTypeSerializer(room_type, data={"is_deleted": True}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return deleteResponse()
        return errorResponse(serializer.errors)
