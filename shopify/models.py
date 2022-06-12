import uuid
from django.db import models


class InventoryType(models.Model):
    type_name = models.CharField(max_length=255)
    type_description = models.TextField(blank=True, null=True)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.type_name


class Inventory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    stock_count = models.PositiveIntegerField(default=0)
    inventory_type = models.ForeignKey(InventoryType, on_delete=models.SET_NULL,
                                       blank=True, null=True)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Inventories"


class ShipmentContainer(models.Model):
    id = models.AutoField(primary_key=True)
    cart_code = models.UUIDField(default=uuid.uuid4)
    added_products = models.ForeignKey(Inventory, on_delete=models.SET_NULL,
                                       db_constraint=False, null=True)
    inventory_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.cart_code)


class Shipment(models.Model):
    shipment_id = models.UUIDField(default=uuid.uuid4)

    # Can use a separate location model for this as well
    shipment_from = models.CharField(max_length=50, blank=True, null=True)
    shipment_to = models.CharField(max_length=50, blank=True, null=True)

    shipment_date = models.DateTimeField()
    inventor_per_shipment = models.ManyToManyField(ShipmentContainer)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipment_id


class ErrorLog(models.Model):
    LOG_TYPE_CHOICES = [("INVENTORY_TYPE", "Inventory Type"),
                        ("INVENTORY", "Inventory"), ]
    STATE_CHOICES = [("CREATE", "CREATE"),
                     ("LIST", "LIST"),
                     ("GET", "GET"),
                     ("UPDATE", "UPDATE"),
                     ("DELETE", "DELETE"), ]
    log_type = models.CharField(
        max_length=25, choices=LOG_TYPE_CHOICES, default="INVENTORY")
    request_data = models.JSONField(blank=True, null=True)
    response_data = models.JSONField(blank=True, null=True)
    misc_data = models.TextField(blank=True, null=True)

    state = models.CharField(
        max_length=25, choices=STATE_CHOICES, default="CREATE")

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.log_type
