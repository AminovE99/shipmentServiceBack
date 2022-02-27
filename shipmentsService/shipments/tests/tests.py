import pytest
from django.conf import settings

from shipments.models import Shipment


@pytest.mark.django_db(transaction=True)
def test_retrieve_shipment(api_client):
    shipment = Shipment.objects.create(departure_address='test_departure_address',
                                       destination_address='test_destination_address')
    response = api_client.get(path=f'{settings.API_PREFIX}/shipment/{shipment.pk}')
    assert response.status_code == 200
    r_data = response.json()
    assert r_data['id'] == shipment.pk
