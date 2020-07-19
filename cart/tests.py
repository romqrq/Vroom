from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from cart.views import view_cart, add_to_cart, adjust_cart


# URLS
class TestCartUrls(SimpleTestCase):

    def test_view_cart_url_is_resolved(self):
        url = reverse('view_cart')
        self.assertEqual(resolve(url).func, view_cart)

    def test_add_to_cart_url_is_resolved(self):
        url = reverse('add_to_cart',
                      kwargs={'item_type': 'car', 'item_id': 2})
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_adjust_cart_url_is_resolved(self):
        url = reverse('adjust_cart',
                      kwargs={'item_type': 'car', 'item_id': 2})
        self.assertEqual(resolve(url).func, adjust_cart)
