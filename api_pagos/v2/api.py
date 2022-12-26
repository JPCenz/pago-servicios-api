from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .serializers import ExpiredPaymentsSerializer, PaymentUserSerializer, ServiceSerializer
from ..models import ExpiredPayments, PaymentUser, Service
from django_filters.rest_framework import DjangoFilterBackend
from .paginacion import StandardResultsSetPagination
from .utils import is_payment_expired



class PaymentUserViewSet(ModelViewSet):
    serializer_class = PaymentUserSerializer
    queryset = PaymentUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('payment_date','expiration_date','service','user')
    throttle_scope = 'payment'
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list" or "retrieve":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):

        #Busca los pagos que hayan expirado segun la fecha de hoy cada vez que hace get 
        for e in PaymentUser.objects.all().order_by('id'):
            print(e.expiration_date)
            is_expired_exists = ExpiredPayments.objects.filter(payment_user=e).exists()
            if is_payment_expired(e.expiration_date) and not is_expired_exists:
                instance =ExpiredPayments(payment_user=e,penalty_fee_amount=e.amount*1.2)
                instance.save()
                print("PAGO GUARDADO",instance)
                
        return super().list(request, *args, **kwargs)


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    throttle_scope = 'service'
    pagination_class= StandardResultsSetPagination

    
    def get_permissions(self):
        if self.action == "list" or "retrieve":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create" or "update":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class ExpiredPaymentsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ExpiredPaymentsSerializer
    queryset = ExpiredPayments.objects.all()
    throttle_scope = 'expired'
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list" or "retrieve":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


