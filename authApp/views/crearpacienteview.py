from urllib import request, response
from rest_framework import status, views
from rest_framework.response import Response
from authApp import serializers

from authApp.serializers.pacienteserializer import PacienteSerializer

class CrearPacienteView(views.APIView):
    def post(self,request):
        serializers = PacienteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return response(serializers.data, status=status.HTTP_201_CREATED)
        return response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)