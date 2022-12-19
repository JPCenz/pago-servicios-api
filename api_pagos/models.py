from django.db import models
from users.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    logo = models.CharField(max_length=400)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name}"


class PaymentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ["-id"]


class ExpiredPayments(models.Model):
    payment_user = models.OneToOneField(PaymentUser, on_delete=models.CASCADE)
    penalty_fee_amount = models.FloatField()

    class Meta:
        ordering = ["-id"]
