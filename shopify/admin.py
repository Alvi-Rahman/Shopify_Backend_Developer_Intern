from django.contrib import admin
from .models import *


class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ["log_type",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["log_type",]

    list_filter = ['log_type', ]


admin.site.register(InventoryType)
admin.site.register(Inventory)
admin.site.register(ErrorLog, ErrorLogAdmin)


