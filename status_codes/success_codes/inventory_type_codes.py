from utils.response_base import CodeObject

INVENTORY_TYPE_CREATE_SUCCESS = CodeObject(
    http_status=200,
    state_code="ITS2001",
    state_message={
        "en": "Inventory Type Create Success"
    }
)

INVENTORY_TYPE_FETCH_SUCCESS = CodeObject(
    http_status=200,
    state_code="IFS2002",
    state_message={
        "en": "Inventory Type Fetch Success"
    }
)

INVENTORY_TYPE_RETRIEVE_SUCCESS = CodeObject(
    http_status=200,
    state_code="IRS2003",
    state_message={
        "en": "Inventory Type Retrieve Success"
    }
)

INVENTORY_TYPE_UPDATE_SUCCESS = CodeObject(
    http_status=200,
    state_code="IUS2004",
    state_message={
        "en": "Inventory Type Update Success"
    }
)

INVENTORY_TYPE_DELETE_SUCCESS = CodeObject(
    http_status=200,
    state_code="IDS2004",
    state_message={
        "en": "Inventory Type Delete Success"
    }
)
