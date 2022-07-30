from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from hotelapi import models
from hotelapi.models import Dishes
from hotelapi.serializers import HotelSerializers,HotelModelSerializer
from rest_framework import status

class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serialize=HotelSerializers(qs,many=True)
        return Response(data=serialize.data)

    def post(self,request,*args,**kwargs):
        serializer=HotelSerializers(data=request.data)
        if serializer.is_valid():
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)

#url:localhost:8000/hotel/menu/{id}/
class DishesDetailView(APIView):
    def get(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            qs=Dishes.objects.get(id=id)
            serializer=HotelSerializers(qs)
            return Response(serializer.data)
        except:
            return Response({"msg":"object doesnot exist"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            object=Dishes.objects.get(id=id)
            serializer=HotelSerializers(data=request.data)
            if serializer.is_valid():
                object.name=serializer.validated_data.get("name")
                object.category=serializer.validated_data.get("category")
                object.price=serializer.validated_data.get("price")
                object.save()
                return Response(data=serializer.data)
        except:
            return Response({"msg": "object doesnot exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,*args,**kwargs):
        try:
            id=kwargs.get("id")
            object=Dishes.objects.get(id=id)
            object.delete()
            return Response({"msg":"Deleted"})
        except:
            return Response({"msg": "object doesnot exist"}, status=status.HTTP_404_NOT_FOUND)

class DishesModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.get(id=id)
        serializer=HotelModelSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=HotelModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Hotel

