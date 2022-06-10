from django.urls import path
from .views import (InventoryViewSet, InventoryTypeViewSet)

urlpatterns = [
    path('inventory/create/', InventoryViewSet.as_view(
        {
            "post": "create"
        }
    )),
]
