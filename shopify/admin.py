from django.contrib import admin
from .models import *


class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ["type_name",
                    "active_status",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["type_name", ]


class InventoryAdmin(admin.ModelAdmin):
    list_display = ["title",
                    "stock_count",
                    "inventory_type",
                    "active_status",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["title", ]


class ShipmentContainerAdmin(admin.ModelAdmin):
    list_display = ["cart_code",
                    "added_products",
                    "inventory_count", ]


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ["shipment_id",
                    "shipment_from",
                    "shipment_to"
                    "shipment_date",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["log_type", ]

    list_filter = ['log_type', ]


class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ["log_type",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["log_type", ]

    list_filter = ['log_type', ]


admin.site.register(InventoryType, InventoryTypeAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(ShipmentContainer, ShipmentContainerAdmin)
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ErrorLog, ErrorLogAdmin)


