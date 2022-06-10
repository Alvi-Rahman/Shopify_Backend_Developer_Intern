from utils.response_base import CodeObject

INVENTORY_CREATE_SUCCESS = CodeObject(
    http_status=200,
    state_code="ICS2001",
    state_message={
        "en": "Inventory Create Success"
    }
)
