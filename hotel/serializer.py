from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    # def __init__(self,request, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.Meta.depth = self.context.get('depth')

    class Meta:
        model = Hotel
        fields = "__all__"

class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
        depth = 1
