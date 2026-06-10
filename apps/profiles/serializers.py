from rest_framework import serializers
from apps.accounts.models import User
from apps.addresses.models import Addresses
from .models import UserProfile


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['id', 'address', 'city', 'state', 'postal_code', 'country', 'is_default']


class UserDetailSerializer(serializers.ModelSerializer):
    default_address = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'role', 'is_active', 'created_at', 'updated_at', 'default_address']
    
    def get_default_address(self, obj):
        """Get the user's default address"""
        default_address = obj.addresses.filter(is_default=True, deleted_at=None).first()
        if default_address:
            return AddressSerializer(default_address).data
        return None
