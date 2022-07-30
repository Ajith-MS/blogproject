from django.shortcuts import render
from rest_framework.views import APIView
from blogapi.models import Mobiles
from rest_framework.response import Response
from blogapi.serializers import MobileSerializers,MobileModelSerializer
from rest_framework import status
from rest_framework import viewsets


# url:localhost:8000/oxygen/mobiles/
# get:list all mobiles
# post:create a mobile
class MobileView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Mobiles.objects.all()
        serializer = MobileSerializers(qs, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MobileSerializers(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)


# url:localhost:8000/oxygen/mobiles/{id}
class MobileDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            qs = Mobiles.objects.get(id=id)
            serializer = MobileSerializers(qs)
            return Response(serializer.data)
        except:
            return Response({"msg": "Object doesnot Exist!"}, status=status.HTTP_404_NOT_FOUND)

    # url:localhost:8000/oxygen/mobiles/{id}
    # put:
    # data:

    def put(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            object = Mobiles.objects.get(id=id)
            serializer = MobileSerializers(data=request.data)
            if serializer.is_valid():
                object.name = serializer.validated_data.get("name")
                object.price = serializer.validated_data.get("price")
                object.band = serializer.validated_data.get("band")
                object.display = serializer.validated_data.get("display")
                object.processor = serializer.validated_data.get("processor")
                object.save()
                return Response(data=serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({"msg": "Object doesnot Exist!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            id = kwargs.get("id")
            object = Mobiles.objects.get(id=id)
            object.delete()
            return Response({"msg": "Deleted"})
        except:
            return Response({"msg": "Object doesnot Exist!"}, status=status.HTTP_404_NOT_FOUND)

class MobileModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MobileModelDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"msg":"Deleted"})

class MobileViewsSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        object=Mobiles.objects.get(id=id)
        object.delete()
        return Response({"msg":"Deleted"},status=status.HTTP_204_NO_CONTENT)


class MobileModelViewsetView(viewsets.ModelViewSet):
    serializer_class = MobileModelSerializer
    queryset = Mobiles.objects.all()

