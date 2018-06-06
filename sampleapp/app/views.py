from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Sample
from app.serializers import Getserializer, Postserializer

class Sampleview(APIView):
    def get(self, request, format=None):
        data=Sample.objects.all()
        serialdata = Getserializer(data, many=True)
        return Response(serialdata.data)

    def post(self, request, format=None):
        data = request.data
        serialdata = Postserializer(data=data)
        if not serialdata.is_valid():
            raise Exception(serialdata.errors)
        sample_obj = Sample()
        sample_obj.name = data["name"]
        sample_obj.comment = data["comment"]
        sample_obj.save()
        data=Getserializer(sample_obj)
        return Response(data.data)

    def delete(self, request, row_id, format=None):
        data = request.data
        serialdata = Getserializer(data, many=True)
        sample_obj = Sample()
        #sample_obj.name = data["name"]
        #sample_obj.comment =  data["comment"]
        sample_obj.delete(row_id)        
        return Response(sample_obj.data)
       
       

