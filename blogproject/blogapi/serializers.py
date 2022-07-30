from rest_framework import serializers
from blogapi.models import Mobiles

class MobileSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    band=serializers.CharField()
    display=serializers.CharField()
    processor=serializers.CharField()

#object level validation
    def validate(self,data):
        cost=data.get("price")
        if cost<0:
            raise serializers.ValidationError("Invalid price!")
        return data

class MobileModelSerializer(serializers.ModelSerializer):
    class Meta:
        id=serializers.CharField(read_only=True)
        model=Mobiles
        fields=["id","name","price","band","display","processor"]
       # fields=__all__
    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("Invalid Price")
        return data
