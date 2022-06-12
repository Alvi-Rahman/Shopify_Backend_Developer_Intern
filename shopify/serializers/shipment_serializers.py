from rest_framework.serializers import ModelSerializer

from shopify.models import Shipment, ShipmentContainer
from .inventory_serializer import InventoryCreateSerializer


class ShipmentContainerCreateSerializer(ModelSerializer):
    added_products = InventoryCreateSerializer()

    class Meta:
        model = ShipmentContainer
        fields = "__all__"


class ShipmentCreateSerializer(ModelSerializer):
    inventor_per_shipment = ShipmentContainerCreateSerializer(many=True)

    class Meta:
        model = Shipment
        fields = "__all__"
