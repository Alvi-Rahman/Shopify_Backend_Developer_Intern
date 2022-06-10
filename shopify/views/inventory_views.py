from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shopify.models import ErrorLog
from shopify.serializers import (InventoryCreateSerializer,
                                 InventoryGetSerializer,)
from status_codes import error_codes, success_codes
from utils.response_utils import ResponseWrapper


class InventoryViewSet(ModelViewSet):
    response_wrapper = ResponseWrapper()
    language = "en"

    def get_serializer_class(self):
        if self.action == "create":
            return InventoryCreateSerializer
        return InventoryCreateSerializer

    def create(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                ErrorLog.objects.create(
                    log_type="INVENTORY",
                    request_data=request.data,
                    response_data=serializer.errors
                )

                error_codes.MISSING_FIELD_DATA.set_state_message({self.language: serializer.errors})
                return Response(
                    **self.response_wrapper.formatted_output_error(error_codes.MISSING_FIELD_DATA, self.language))

            self.perform_create(serializer)

            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_CREATE_SUCCESS,
                data=InventoryGetSerializer(instance=serializer.instance).data,
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="INVENTORY",
                request_data=request.data,
                response_data=e.args
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))


