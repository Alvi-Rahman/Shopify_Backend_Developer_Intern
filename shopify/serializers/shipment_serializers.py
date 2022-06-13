from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from shopify.models import Shipment, ShipmentContainer, Inventory
from shopify.serializers import InventoryGetSerializer


class ShipmentContainerCreateSerializer(Serializer):
    added_products = serializers.IntegerField()
    inventory_count = serializers.IntegerField()


class ShipmentContainerMakeSerializer(ModelSerializer):

    class Meta:
        model = ShipmentContainer
        exclude = ("id", "cart_code", )


class ShipmentContainerGetSerializer(ModelSerializer):
    added_products = InventoryGetSerializer()

    class Meta:
        model = ShipmentContainer
        exclude = ("id", "cart_code",)

class ShipmentCreateSerializer(ModelSerializer):
    inventory_per_shipment = ShipmentContainerCreateSerializer(many=True)

    class Meta:
        model = Shipment
        fields = "__all__"


class ShipmentGetSerializer(ModelSerializer):
    inventory_per_shipment = ShipmentContainerGetSerializer(many=True)

    class Meta:
        model = Shipment
        exclude = ("id",)

