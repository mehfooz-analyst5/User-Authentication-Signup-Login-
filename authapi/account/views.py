from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .serializers import UserRegistrationSerializer
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
