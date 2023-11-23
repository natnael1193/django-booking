from rest_framework import serializers
from room_quantity.models import RoomQuantity


class RoomQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomQuantity
        fields = "__all__"
class RoomQuantityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomQuantity
        fields = "__all__"
        depth = 1
