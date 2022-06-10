from django.urls import path
from .views import (InventoryViewSet, InventoryTypeViewSet)

inventory_type_urlpatterns = [
    path('inventory-type/create/', InventoryTypeViewSet.as_view({"post": "create"}),
         name="inventory_type_create"),
    path('inventory-type/all/', InventoryTypeViewSet.as_view({"get": "list"}),
         name="inventory_type_list"),
    path("inventory-type/<int:id>/", InventoryTypeViewSet.as_view(
        {
            "get": "retrieve",
            "patch": "partial_update",
            "delete": "destroy",
        }
    )),
]

inventory_urlpatterns = [
    path('inventory/create/', InventoryViewSet.as_view({"post": "create"}),
         name="inventory_create"),
    path('inventory/all/', InventoryViewSet.as_view({"get": "list"}),
         name="inventory_type_list"),
    path("inventory/<int:id>/", InventoryViewSet.as_view(
        {
            "get": "retrieve",
            "patch": "partial_update",
            "delete": "destroy",
        }
    )),
]

urlpatterns = inventory_type_urlpatterns + inventory_urlpatterns
