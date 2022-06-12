from rest_framework.serializers import ModelSerializer

from shopify.models import Shipment, ShipmentContainer
from .inventory_serializer import InventoryGetSerializer


class ShipmentContainerCreateSerializer(ModelSerializer):
    class Meta:
        model = ShipmentContainer
        fields = "__all__"


class ShipmentContainerGetSerializer(ModelSerializer):
    added_products = InventoryGetSerializer()

    class Meta:
        model = ShipmentContainer
        exclude = ("id",)
