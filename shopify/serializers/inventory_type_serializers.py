from rest_framework.serializers import ModelSerializer
from shopify.models import InventoryType


class InventoryTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        fields = "__all__"


class InventoryTypeGetSerializer(ModelSerializer):
    class Meta:
        model = InventoryType
        exclude = ("id",)
