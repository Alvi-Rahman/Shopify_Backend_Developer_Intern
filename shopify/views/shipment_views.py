from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shopify.models import ErrorLog, Shipment
from shopify.serializers import (ShipmentCreateSerializer,
                                 ShipmentGetSerializer,
                                 ShipmentContainerMakeSerializer, )
from status_codes import success_codes, error_codes
from utils.pagination_utils import CustomLimitPagination
from utils.response_utils import ResponseWrapper


class ShipmentViewSet(ModelViewSet):
    response_wrapper = ResponseWrapper()
    language = "en"
    queryset = Shipment.objects.all()
    pagination_class = CustomLimitPagination
    lookup_field = "id"

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
        if self.action == "create" or self.action == "partial_update":
            return ShipmentCreateSerializer
        return ShipmentGetSerializer

    def create(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                ErrorLog.objects.create(
                    log_type="SHIPMENT",
                    request_data=request.data,
                    response_data=serializer.errors,
                    state="CREATE"
                )

                error_codes.MISSING_FIELD_DATA.set_state_message({self.language: serializer.errors})
                return Response(
                    **self.response_wrapper.formatted_output_error(error_codes.MISSING_FIELD_DATA, self.language))

            inventory_per_shipment = serializer.validated_data.pop("inventory_per_shipment")

            shipment_container_serializer = ShipmentContainerMakeSerializer(data=inventory_per_shipment, many=True)

            if not shipment_container_serializer.is_valid():
                ErrorLog.objects.create(
                    log_type="SHIPMENT",
                    request_data=request.data,
                    response_data=shipment_container_serializer.errors,
                    state="CREATE"
                )
                error_codes.MISSING_FIELD_DATA.set_state_message({self.language: shipment_container_serializer.errors})
                return Response(
                    **self.response_wrapper.formatted_output_error(error_codes.MISSING_FIELD_DATA, self.language))

            shipment_container_serializer.save()

            self.perform_create(serializer)
            serializer.instance.inventory_per_shipment.add(*shipment_container_serializer.instance)

            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_CREATE_SUCCESS,
                data=ShipmentGetSerializer(instance=serializer.instance).data,
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="SHIPMENT",
                request_data=request.data,
                response_data=e.args,
                state="CREATE"
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "date_from", openapi.IN_QUERY, type=openapi.FORMAT_DATE),
            openapi.Parameter(
                "date_to", openapi.IN_QUERY, type=openapi.FORMAT_DATE),
        ]
    )
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()

            date_from = request.query_params.get('date_from')
            date_to = request.query_params.get('date_to')
            if date_from is not None and date_to is not None:
                try:
                    date_from = timezone.datetime.strptime(
                        date_from, "%Y-%m-%d").date()
                    date_to = timezone.datetime.strptime(
                        date_to, "%Y-%m-%d").date()
                    date_to += timezone.timedelta(days=1)
                except ValueError:
                    return Response(
                        **self.response_wrapper.formatted_output_error(error_codes.INVALID_DATE, self.language))
                queryset = queryset.filter(created_at__range=[date_from, date_to])

            page = self.paginate_queryset(queryset)
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)

            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_FETCH_SUCCESS,
                data=paginated_response.data,
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="SHIPMENT",
                request_data=request.data,
                response_data=e.args,
                state="LIST"
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if not instance:
                return Response(**self.response_wrapper.formatted_output_error(
                    error_codes.INVENTORY_NOT_FOUND, self.language))
            serializer = self.get_serializer(instance, many=False)
            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_RETRIEVE_SUCCESS,
                data=serializer.data,
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="SHIPMENT",
                request_data=request.data,
                response_data=e.args,
                state="GET"
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if not serializer.is_valid():
                ErrorLog.objects.create(
                    log_type="SHIPMENT",
                    request_data=request.data,
                    response_data=serializer.errors,
                    state="UPDATE"
                )

                error_codes.MISSING_FIELD_DATA.set_state_message({self.language: serializer.errors})
                return Response(
                    **self.response_wrapper.formatted_output_error(error_codes.MISSING_FIELD_DATA, self.language))

            self.perform_update(serializer)

            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_UPDATE_SUCCESS,
                data=ShipmentGetSerializer(instance=serializer.instance).data,
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="SHIPMENT",
                request_data=request.data,
                response_data=e.args,
                state="UPDATE"
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()

            if not instance:
                return Response(**self.response_wrapper.formatted_output_error(
                    error_codes.INVENTORY_NOT_FOUND, self.language))

            self.perform_destroy(instance)

            return Response(**self.response_wrapper.formatted_output_success(
                code=success_codes.INVENTORY_DELETE_SUCCESS,
                data={
                    "inventory_type_id": kwargs.get('id'),
                },
                language=self.language
            ))
        except Exception as e:
            ErrorLog.objects.create(
                log_type="INVENTORY_TYPE",
                request_data=request.data,
                response_data=e.args,
                state="DELETE"
            )
            return Response(**self.response_wrapper.formatted_output_error(error_codes.UNKNOWN_ERROR, self.language))
