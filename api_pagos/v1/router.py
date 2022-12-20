from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payments', api.PaymentUserViewSet)
router.register(r'service', api.ServiceViewSet)


api_urlpatterns = router.urls