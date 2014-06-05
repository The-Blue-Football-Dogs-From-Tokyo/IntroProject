from django.test import TestCase
from sgtioapp import views
# Create your tests here.

class ViewTestCase(TestCase):
    def test_connection(self):
        self.assertEquals(1+1, 2)
    #def test_null():

    #def test_
