from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins, viewsets
from .serializers import ExpiredPaymentsSerializer, PaymentUserSerializer, ServiceSerializer
from ..models import ExpiredPayments, PaymentUser, Service
from django_filters.rest_framework import DjangoFilterBackend



class PaymentUserViewSet(ModelViewSet):
    serializer_class = PaymentUserSerializer
    queryset = PaymentUser.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('payment_date','expiration_date')
    throttle_scope = 'payment'



class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    throttle_scope = 'service'



class ExpiredPaymentsViewSet(ModelViewSet):
    serializer_class = ExpiredPaymentsSerializer
    queryset = ExpiredPayments.objects.all()
    throttle_scope = 'expired'


