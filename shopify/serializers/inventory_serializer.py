from rest_framework.serializers import ModelSerializer

from shopify.models import Inventory
from .inventory_type_serializers import InventoryTypeCreateSerializer


class InventoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryGetSerializer(ModelSerializer):
    inventory_type = InventoryTypeCreateSerializer()

    class Meta:
        model = Inventory
        exclude = ("id",)
