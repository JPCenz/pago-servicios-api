from rest_framework.serializers import ModelSerializer,StringRelatedField
from .. import models

class ServiceSerializer(ModelSerializer):
    class Meta:
        model=models.Service
        fields= "__all__"

class PaymentUserSerializer(ModelSerializer):
    service = StringRelatedField(many=False)
    class Meta:
        model = models.PaymentUser
        fields= "__all__"
        
        # read_only_fields= ("user",)

class ExpiredPayments(ModelSerializer):
    class Meta:
        model = models.ExpiredPayments
        fields="__all__"
        read_only_fields= ('payment_user','penalty_fee_amount',)

