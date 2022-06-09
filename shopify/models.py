from django.db import models

# Create your models here.


class InventoryType(models.Model):
    type_name = models.CharField(max_length=255)
    type_description = models.TextField(blank=True, null=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.type_name

