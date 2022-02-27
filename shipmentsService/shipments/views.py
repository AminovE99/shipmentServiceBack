from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

from shipments.models import Shipment
from shipments.serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Shipment.objects.all()

    serializer_class = ShipmentSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Shipment, pk=pk)
