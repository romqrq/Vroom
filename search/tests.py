from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from search.views import do_search


# URLS
class TestSearchUrls(SimpleTestCase):

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, do_search)
