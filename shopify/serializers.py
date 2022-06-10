from rest_framework.serializers import ModelSerializer
from .models import Inventory, InventoryType


class InventoryTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        fields = "__all__"


class InventoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class GetInventorySerializer(ModelSerializer):
    inventory_type = InventoryTypeCreateSerializer()

    class Meta:
        model = Inventory
        fields = "__all__"
