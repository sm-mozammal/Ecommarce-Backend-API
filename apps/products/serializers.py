import rest_framework.serializers as serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = ['id', 'name', 'description', 'slug', 'is_active']
