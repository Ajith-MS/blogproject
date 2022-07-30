from rest_framework import serializers
from hotelapi.models import Dishes

class HotelSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()

#object level validation
    def validate(self,data):
        cost=data.get("price")
        if cost<0:
            raise serializers.ValidationError("Invalid Price")
        return data


class HotelModelSerializer(serializers.ModelSerializer):
    class Meta:
        id=serializers.CharField(read_only=True)
        model=Dishes
        fields=["id","name","category","price"]
    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("Invalid Price")
        return data