import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase
from .views import *
from .constants import RECEIPT_TEST_DATA_BAD, RECEIPT_TEST_DATA_VALID


class TestReceiptViewSet(TestCase):

    def test_get_receipt(self):
        factory = APIRequestFactory()
        request = factory.get('receipt')
        view = ReceiptView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_receipt_bad_data(self):
        factory = APIRequestFactory()
        request = factory.post('receipt', RECEIPT_TEST_DATA_BAD, format='json')
        view = ReceiptView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_receipt_valid_data(self):
        factory = APIRequestFactory()
        request = factory.post('receipt', RECEIPT_TEST_DATA_VALID, format='json')
        view = ReceiptView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
