from utils.response_base import CodeObject

INVENTORY_TYPE_CREATE_SUCCESS = CodeObject(
    http_status=200,
    state_code="ITS2001",
    state_message={
        "en": "Inventory Type Create Success"
    }
)

INVENTORY_CREATE_SUCCESS = CodeObject(
    http_status=200,
    state_code="ICS2002",
    state_message={
        "en": "Inventory Create Success"
    }
)
