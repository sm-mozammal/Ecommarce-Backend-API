from django.shortcuts import render
from rest_framework import viewsets

from apps.accounts.permissions import IsAdmin
from .models import Category
from .serializers import CategorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdmin()]
        return super().get_permissions()