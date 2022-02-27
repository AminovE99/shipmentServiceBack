from django.test import TestCase, Client

from shipments.choices import Status
from shipments.models import Shipment
from shipmentsService.settings import URL_PREFIX


class ShipmentTestCase(TestCase):
    def setUp(self) -> None:
        self.test_shipment = Shipment.objects.create(departure_address='test_departure_address',
                                                     destination_address='test_destination_address')
        self.client = Client()

    def test_retrieve_shipment(self):
        response = self.client.get(f'/{URL_PREFIX}/shipment/{self.test_shipment.pk}/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], self.test_shipment.pk)

    def test_list_shipment(self):
        response = self.client.get(f'/{URL_PREFIX}/shipment/')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['id'], self.test_shipment.pk)

    def test_create_shipment_success(self):
        response = self.client.post(f'/{URL_PREFIX}/shipment/',
                                    data={'departure_address': 'test_departure_address2',
                                          'destination_address': 'test_destination_address2',
                                          'status': Status.DRAFT.value})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(Shipment.objects.count(), 2)
        self.assertEqual(data['departure_address'], 'test_departure_address2')
        self.assertEqual(data['destination_address'], 'test_destination_address2')

    def test_create_shipment_400(self):
        response = self.client.post(f'/{URL_PREFIX}/shipment/', data={'departure_address': 'test_departure_address2',
                                                                      'destination_address': 'test_destination_address2',
                                                                      'status': 'NOT A STATUS'})
        self.assertEqual(response.status_code, 400)

    def test_update_shipment_success(self):
        old_departure_address = self.test_shipment.departure_address
        new_departure_address = 'test_new_departure_address'
        response = self.client.patch(f'/{URL_PREFIX}/shipment/{self.test_shipment.pk}/',
                                     data={'departure_address': new_departure_address}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotEqual(old_departure_address, data['departure_address'])
        self.assertEqual(new_departure_address, data['departure_address'])

    def test_delete_shipment_success(self):
        response = self.client.delete(f'/{URL_PREFIX}/shipment/{self.test_shipment.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(0, Shipment.objects.count())
