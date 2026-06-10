from venv import logger

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from .utils import get_tokens
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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
            user = serializer.validated_data
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
                        'phone': user.phone,
                        'refresh_token': token['refresh'],
                        'access_token': token['access'],
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


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            
            # If refresh token is provided, blacklist it
            if refresh_token:
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except Exception as e:
                    return Response({
                        'status': 'error',
                        'message': f'Invalid refresh token: {str(e)}',
                    }, status=status.HTTP_400_BAD_REQUEST)
            
            # User is authenticated via access token (Bearer token)
            # Return success - client should discard access token
            return Response({
                'status': 'success',
                'message': 'User logged out successfully',
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Logout failed: {str(e)}',
            }, status=status.HTTP_400_BAD_REQUEST)
