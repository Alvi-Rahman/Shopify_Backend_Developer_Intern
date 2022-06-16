from django.db import transaction
from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from shopify.models import Shipment, ShipmentContainer, Inventory
from shopify.serializers import InventoryGetSerializer


class ShipmentContainerCreateSerializer(Serializer):
    added_products = serializers.IntegerField()
    inventory_count = serializers.IntegerField()


class ShipmentContainerMakeListSerializer(serializers.ListSerializer):
    def run_validation(self, data=empty):
        # added_products_dict = {}
        with transaction.atomic():
            for attr in data:
                # _pk = attr["added_products"]
                # if _pk not in added_products_dict:
                #     added_products_dict[_pk] = attr["inventory_count"]
                # else:
                #     added_products_dict[_pk] += attr["inventory_count"]

                inventory = Inventory.objects.get(pk=attr["added_products"])
                if inventory.stock_count < attr["inventory_count"]:
                    raise serializers.ValidationError(f"Insufficient Stock for {inventory.title}")

                inventory.stock_count = inventory.stock_count - attr["inventory_count"]

                inventory.save()
                inventory.refresh_from_db()

        return super(ShipmentContainerMakeListSerializer, self).run_validation(data)


class ShipmentContainerMakeSerializer(ModelSerializer):

    class Meta:
        model = ShipmentContainer
        list_serializer_class = ShipmentContainerMakeListSerializer
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

