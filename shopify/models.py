from django.db import models

# Create your models here.


class InventoryType(models.Model):
    type_name = models.CharField(max_length=255)
    type_description = models.TextField(blank=True, null=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.type_name


class Inventory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    stock_count = models.PositiveIntegerField(default=0)
    inventory_type = models.ForeignKey(InventoryType, on_delete=models.CASCADE)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Inventories"
