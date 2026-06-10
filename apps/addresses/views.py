from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AddressesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Addresses


# Create your views here.
class AddressesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            # Get single address
            try:
                address = Addresses.objects.get(pk=pk, user=request.user, deleted_at=None)
                serializer = AddressesSerializer(address)
                return Response({
                    'status': 'success',
                    'message': 'Address retrieved successfully',
                    'data': serializer.data,
                }, status=status.HTTP_200_OK)
            except Addresses.DoesNotExist:
                return Response({
                    'status': 'error',
                    'message': 'Address not found',
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    'status': 'error',
                    'message': f'Error retrieving address: {str(e)}',
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Get all addresses
            addresses = Addresses.objects.filter(user=request.user, deleted_at=None)
            serializer = AddressesSerializer(addresses, many=True)
            return Response({
                'status': 'success',
                'message': 'Addresses retrieved successfully',
                'data': serializer.data,
            }, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AddressesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'status': 'success',
                'message': 'Address created successfully',
                'data': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'error',
            'message': 'Address creation failed',
            'errors': serializer.errors,    
        }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if not pk:
            return Response({
                'status': 'error',
                'message': 'Address ID is required',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            address = Addresses.objects.get(pk=pk, user=request.user, deleted_at=None)
            serializer = AddressesSerializer(address, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Address updated successfully',
                    'data': serializer.data,
                }, status=status.HTTP_200_OK)
            return Response({
                'status': 'error',
                'message': 'Address update failed',
                'errors': serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)
        except Addresses.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Address not found',
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error updating address: {str(e)}',
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if not pk:
            return Response({
                'status': 'error',
                'message': 'Address ID is required',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            address = Addresses.objects.get(pk=pk, user=request.user, deleted_at=None)
            address.deleted_at = timezone.now()
            address.save()
            return Response({
                'status': 'success',
                'message': 'Address deleted successfully',
            }, status=status.HTTP_200_OK)
        except Addresses.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Address not found',
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Error deleting address: {str(e)}',
            }, status=status.HTTP_400_BAD_REQUEST)

