from django.test import TestCase
from stagioapp import views
# Create your tests here.

class ViewTestCase(TestCase):
	def view_test(self):
		views.function():
