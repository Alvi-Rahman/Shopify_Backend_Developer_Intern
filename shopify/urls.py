from django.urls import path
from .views import (InventoryViewSet, InventoryTypeViewSet)

urlpatterns = [
    path('inventory/create/', InventoryViewSet.as_view(
        {
            "post": "create",
        }
    )),
    path('inventory-type/create/', InventoryTypeViewSet.as_view(
        {
            "post": "create"
        }
    )),
    path('inventory-type/all/', InventoryTypeViewSet.as_view(
        {
            "get": "list"
        }
    )),
    path("inventory-type/<int:id>/", InventoryTypeViewSet.as_view(
        {"get": "retrieve"}
    )),
]
