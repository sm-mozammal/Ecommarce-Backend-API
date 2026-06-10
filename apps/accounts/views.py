from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from .utils import get_tokens

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data =request.data)

        if serializer.is_valid():
            user = serializer.save()
            token  = get_tokens(user)
            return Response(
                {
                    'status': 'success',
                    'message': 'User registered successfully',
                    'data': serializer.data,
                    'token': token,
                },
                status = status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': 'error',
                'message': 'User registration failed',
                'errors': serializer.errors,
            },
            status = status.HTTP_400_BAD_REQUEST
        )



class LoginView(APIView):
    def post (self, request):
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.validatedd_data
            token = get_tokens(user)
            return Response(
                {
                    'status': 'success',
                    'message': 'User logged in successfully',
                    'data': {
                        'id': user.id,
                        'email': user.email,
                        'name': user.name,
                        'role': user.role,
                        'token': token,
                    },
                }
            )
        
        return Response(
            {
                'status': 'error',
                'message': 'User login failed',
                'errors': serializer.errors,
            },
            status = status.HTTP_400_BAD_REQUEST
        )

