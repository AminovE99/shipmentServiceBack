from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer, ShipmentRetrieveSerializer


class ShipmentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Shipment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        return ShipmentRetrieveSerializer if self.action in ['list', 'retrieve'] else ShipmentSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Shipment, pk=pk)
