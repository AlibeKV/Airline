from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import Airplaneserializer , PlaneSerializer
from apps.airline.models import Airplane

from apps.plane.models import Plane

class ArplanAPIView(APIView):

    def get(self,request):
        airplane = Airplane.objects.all()
        serilizer = Airplaneserializer(airplane, many=True)
        return Response(serilizer.data,status=HTTP_200_OK)
    
    def get(self,request):
        serilizer = Airplaneserializer(request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=HTTP_201_CREATED)
        return Response(serilizer.errors,status=HTTP_400_BAD_REQUEST)



class AiplaneDetailAPIView(APIView):

    def get(self,request,pk):
        airplane = Airplane.objects.get(pk=pk)
        serilizer = Airplaneserializer(airplane,)
        return Response(serilizer.data,status=HTTP_200_OK)
    
    def patch(self, request, pk):
        airplane = Airplane.objects.get(pk=pk)
        serilizer = Airplaneserializer(airplane,data=request.data, partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response(
                serilizer.data,status=HTTP_202_ACCEPTED)
        return Response(serilizer._errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        airplane =Airplane.objects.get(pk=pk)
        airplane.delete()
        return Response('Delete',status=HTTP_204_NO_CONTENT)
    
#---------------------------------------------------------------------------------------------

class PlaneAPIView(APIView):

    def get(self,request):
        plane = Plane.objects.all()
        serilizer = PlaneSerializer(plane, many=True)
        return Response(serilizer.data,status=HTTP_200_OK)
    
    def get(self,request):
        serilizer = PlaneSerializer(request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=HTTP_201_CREATED)
        return Response(serilizer.errors,status=HTTP_400_BAD_REQUEST)



class PlaneDetailAPIView(APIView):

    def get(self,request,pk):
        plane = Plane.objects.get(pk=pk)
        serilizer = PlaneSerializer(plane)
        return Response(serilizer.data,status=HTTP_200_OK)
    
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serilizer = PlaneSerializer(plane,data=request.data, partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response(
                serilizer.data,status=HTTP_202_ACCEPTED)
        return Response(serilizer._errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        plane = Plane.objects.get(pk=pk)
        plane.delete()
        return Response('Delete',status=HTTP_204_NO_CONTENT)