from django.shortcuts import render
from .views import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Administrator
from .serializers import AdministratorSerializer
from rest_framework import status

# Create your views here.
class CreateAdministratorView(APIView):
    def post(self, request):
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AdministratorDetailView(APIView):
    def get(self, request, pk):
        try:
            administrator = Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            return Response({"error": "Administrator not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdministratorSerializer(administrator)
        return Response(serializer.data)
            
class AdministratorListView(APIView):
    def get(self, request):
        administrators = Administrator.objects.all()
        serializer = AdministratorSerializer(administrators, many=True)
        return Response(serializer.data)          
    
class UpdateAdministratorView(APIView):
    def get(self, request, pk):
        try:
            administrator = Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            return Response({"error": "Administrator not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdministratorSerializer(administrator)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            administrator = Administrator.objects.get(pk=pk)
        except Administrator.DoesNotExist:
            return Response({"error": "Administrator not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdministratorSerializer(administrator, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  