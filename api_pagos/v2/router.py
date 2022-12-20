from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'paymentuser', api.PaymentUserViewSet)
router.register(r'service', api.ServiceViewSet)
router.register(r'expired', api.ExpiredPaymentsViewSet)

api_urlpatterns = router.urls
