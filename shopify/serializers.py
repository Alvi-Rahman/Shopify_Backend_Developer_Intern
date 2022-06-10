from rest_framework.serializers import ModelSerializer
from .models import Inventory, InventoryType


class InventoryTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        fields = "__all__"


class InventoryTypeGetSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        exclude = ("id",)


class InventoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryGetSerializer(ModelSerializer):
    inventory_type = InventoryTypeCreateSerializer()

    class Meta:
        model = Inventory
        exclude = ("id",)
