from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .serializers import ExpiredPaymentsSerializer, PaymentUserSerializer, ServiceSerializer
from ..models import ExpiredPayments, PaymentUser, Service
from django_filters.rest_framework import DjangoFilterBackend
from .paginacion import StandardResultsSetPagination



class PaymentUserViewSet(ModelViewSet):
    serializer_class = PaymentUserSerializer
    queryset = PaymentUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('payment_date','expiration_date','service','user')
    throttle_scope = 'payment'
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                AllowAny,
            ]
        elif self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]



class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    throttle_scope = 'service'
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        # elif self.action == "create":
        #     permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]



class ExpiredPaymentsViewSet(ModelViewSet):
    serializer_class = ExpiredPaymentsSerializer
    queryset = ExpiredPayments.objects.all()
    throttle_scope = 'expired'
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


