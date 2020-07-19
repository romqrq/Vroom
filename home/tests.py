from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from home.views import about_view, faqs_view, contact_view


# URLS
class TestHomeUrls(SimpleTestCase):

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about_view)

    def test_faqs_url_is_resolved(self):
        url = reverse('faqs')
        self.assertEqual(resolve(url).func, faqs_view)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact_view)
