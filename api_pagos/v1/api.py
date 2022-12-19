from rest_framework.viewsets import ViewSet,ModelViewSet,GenericViewSet
from rest_framework import views,status
from ..models import PaymentUser,Service,ExpiredPayments
from .serializers import PaymentUserSerializer,ServiceSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend



class PaymentUserViewSet(GenericViewSet):
    queryset = PaymentUser.objects.all().order_by('-id')
    serializer_class= PaymentUserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('service','payment_date','user')

    def get_throttles(self):
        if self.action == "create":
            # aca vamos a decir que use el throttle_scope
            self.throttle_scope = "create_payment"
        return super().get_throttles()


    def list(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer =PaymentUserSerializer(queryset,many= True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        payment= get_object_or_404(self.queryset, pk=pk)
        serializer =PaymentUserSerializer(payment)
        return Response(serializer.data)

    def create(self,request,*args, **kwargs):
        serializer = PaymentUserSerializer(data= request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"ok": True, "message": serializer.data},
            status=status.HTTP_201_CREATED)
        return Response(
            {"ok": False, "message": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class= ServiceSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'description')





