from rest_framework.serializers import ModelSerializer,StringRelatedField, PrimaryKeyRelatedField
from .. import models
import datetime

class ServiceSerializer(ModelSerializer):
    class Meta:
        model=models.Service
        fields= "__all__"
        ref_name="service_v1"

class PaymentUserSerializer(ModelSerializer):
    # service = StringRelatedField(many=False,read_only=False)
    class Meta:
        model = models.PaymentUser
        fields= "__all__"
        ref_name="payment_v1"
        # read_only_fields= ("expiration_date",)
    # def create(self, validated_data:dict):
    #     p = validated_data.get("payment_date")
    #     validated_data["expiration_date"]= p + datetime.timedelta(days=30)
    #     payment = super().create(validated_data)
        
    #     return payment
        

class ExpiredPaymentsSerializer(ModelSerializer):
    paymnet_user = PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = models.ExpiredPayments
        fields="__all__"
        ref_name="expired_v1"
        #read_only_fields= ('payment_user','penalty_fee_amount',)

