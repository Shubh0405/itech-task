from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

# Create your views here.

class RegisterView(APIView):

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class LoginAPIView(APIView):

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

class LogoutAPIView(APIView):
    permissions_classes = [permissions.IsAuthenticated,]

    def post(self,request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Logged out successfully!'},status=201)
        return Response(serializer.errors,status=400)
