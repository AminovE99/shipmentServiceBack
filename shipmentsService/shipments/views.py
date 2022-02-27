from rest_framework import viewsets, mixins

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer, ShipmentRetrieveSerializer


class ShipmentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Shipment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        return ShipmentRetrieveSerializer if self.action in ['list', 'retrieve'] else ShipmentSerializer
