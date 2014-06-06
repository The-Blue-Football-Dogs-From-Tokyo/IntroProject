from django.test import TestCase
from sgtioapp import views
from django.test.client import Client
import requests
# Create your tests here.

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_connection(self):
        response = self.client.get('/sgtioapp/')
        self.assertEquals(200, response.status_code)

    def test_search(self):
        response = self.client.get('/sgtioapp/?search=iphone')
        self.assertEquals(200, response.status_code)
        self.assertNotEquals(response.content, None)
