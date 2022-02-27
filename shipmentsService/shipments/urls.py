from rest_framework.routers import SimpleRouter

from shipments.views import ShipmentViewSet

router = SimpleRouter()
router.register(r'shipment', ShipmentViewSet, basename='shipment')

urlpatterns = router.urls
