from utils.response_base import CodeObject

MISSING_FIELD_DATA = CodeObject(
    http_status=400,
    state_code="MFD4001",
    state_message={
        "en": "Not all fields are provided properly."
    }
)

INVENTORY_TYPE_NOT_FOUND = CodeObject(
    http_status=400,
    state_code="ITN4002",
    state_message={
        "en": "Specified Inventory Type Not Found."
    }
)

INVENTORY_NOT_FOUND = CodeObject(
    http_status=400,
    state_code="INF4003",
    state_message={
        "en": "Specified Inventory Type Not Found."
    }
)

INVALID_DATE = CodeObject(
    http_status=400,
    state_code="ITN4004",
    state_message={
        "en": "Specified Inventory Type Not Found."
    }
)

UNKNOWN_ERROR = CodeObject(
    http_status=400,
    state_code="UNK5005",
    state_message={
        "en": "Something Went Wrong."
    }
)
