from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shopify.models import ErrorLog, Inventory
from shopify.serializers import (InventoryCreateSerializer,
                                 InventoryGetSerializer,)
from status_codes import error_codes, success_codes
from utils.response_utils import ResponseWrapper


class InventoryViewSet(ModelViewSet):
    response_wrapper = ResponseWrapper()
    language = "en"

    queryset = Inventory.objects.all()

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = queryset.filter(**filter_kwargs).first()

        return obj

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


