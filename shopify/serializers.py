from rest_framework.serializers import ModelSerializer
from .models import Inventory, InventoryType


class InventoryTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        fields = "__all__"


