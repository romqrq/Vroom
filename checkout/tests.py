from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from checkout.views import checkout


# URLS
class TestCheckoutUrls(SimpleTestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)
