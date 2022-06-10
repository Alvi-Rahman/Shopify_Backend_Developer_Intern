from utils.response_base import CodeObject

MISSING_FIELD_DATA = CodeObject(
    http_status=400,
    state_code="MFD4001",
    state_message={
        "en": "Not all fields are provided properly."
    }
)

UNKNOWN_ERROR = CodeObject(
    http_status=400,
    state_code="UNK5001",
    state_message={
        "en": "Something Went Wrong."
    }
)
