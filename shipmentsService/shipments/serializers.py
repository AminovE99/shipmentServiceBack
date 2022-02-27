from rest_framework import serializers

from shipments.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'departure_address', 'destination_address', 'status')


class ShipmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id', 'created_at', 'delivered_at', 'departure_address', 'destination_address', 'status')
