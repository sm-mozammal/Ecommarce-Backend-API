import rest_framework.serializers as serializers
from .models import Addresses

class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
        read_only_fields = ['id','user', 'created_at']