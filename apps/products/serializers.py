import rest_framework.serializers as serializers
from .models import Category, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'description', 'image', 'slug', 'is_active', 'created_at', 'updated_at']



class BrandSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brand
        fields = ['id', 'name', 'image', 'created_at', 'updated_at']
