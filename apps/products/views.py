from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.accounts.permissions import IsAdmin
from .models import Category, Brand
from .serializers import CategorySerializer, BrandSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(deleted_at=None)
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'status'        : 'success',
            'message'       : 'Categories retrieved successfully',
            'data'          : serializer.data,
        }, status=200)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.deleted_at is not None:
            return Response({
                'status': 'error',
                'message': 'Category not found',
            }, status=404)
        serializer = self.get_serializer(instance)
        return Response({
            'status': 'success',
            'message': 'Category retrieved successfully', 
            'data': serializer.data      
            })
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':'success',
                'message':"Category created successfully",
                'data':serializer.data
            }, status=201)
        return Response({
            'status':'error',       
            'message':"Category creation failed",
            'errors':serializer.errors
        }, status=400)
            
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'message': 'Category updated successfully',
                'data': serializer.data,
            }, status=200)
        return Response({
            'status': 'error',
            'message': 'Category update failed',
            'errors': serializer.errors,
        }, status=400)



        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            if instance.deleted_at is not None:
                return Response ({
                    'status': 'error',
                    'message': 'Category not found',
                }, status=404)
                
                instance.deleted_at = timezone.now()
                instance.save()

                return Response({
                    'status': 'success',
                    'message': 'Category deleted successfully',
                })

    

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()


    def list(self, request , *args, **kwargs):
        queryset = self.get_queryset().filter(deleted_at = None)
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'status':'success','message':'Brands retrieved successfully','data':serializer.data}, status=200)
        