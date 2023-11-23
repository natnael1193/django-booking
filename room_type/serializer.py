from rest_framework import serializers

from room_type.models import RoomType


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"

class RoomTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = "__all__"
        depth = 1
