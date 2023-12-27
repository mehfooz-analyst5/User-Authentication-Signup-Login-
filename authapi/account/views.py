from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_202_ACCEPTED

from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import User


"""
Making Api for User Registration and user login.
"""


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'mg':'Registration Successfull'}, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                return Response({'mg':'Login Successfull'}, status=HTTP_202_ACCEPTED)

            else:
                return Response({
                    'errors': {'non_field_errors' : ['Email or Password is not valid']}
                }, status=HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)