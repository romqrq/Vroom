from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cars.views import all_cars, custom_classic_only, luxury_only, supersport_only, car_register, car_detail, car_edit_view, del_car, add_ons


class TestCarsUrls(SimpleTestCase):

    def test_all_cars_url_is_resolved(self):
        url = reverse('all_cars')
        self.assertEqual(resolve(url).func, all_cars)

    def test_custom_classic_only_url_is_resolved(self):
        url = reverse('custom_classic_only')
        self.assertEqual(resolve(url).func, custom_classic_only)

    def test_luxury_only_url_is_resolved(self):
        url = reverse('luxury_only')
        self.assertEqual(resolve(url).func, luxury_only)

    def test_supersport_only_url_is_resolved(self):
        url = reverse('supersport_only')
        self.assertEqual(resolve(url).func, supersport_only)

    def test_car_register_url_is_resolved(self):
        url = reverse('car_register')
        self.assertEqual(resolve(url).func, car_register)

    def test_car_detail_url_is_resolved(self):
        url = reverse('car_detail', kwargs={'car_id': 2})
        self.assertEqual(resolve(url).func, car_detail)

    def test_edit_car_url_is_resolved(self):
        url = reverse('edit_car', kwargs={'car_id': 2})
        self.assertEqual(resolve(url).func, car_edit_view)

    def test_delete_car_url_is_resolved(self):
        url = reverse('delete_car', kwargs={'car_id': 2})
        self.assertEqual(resolve(url).func, del_car)

    def test_add_ons_url_is_resolved(self):
        url = reverse('add_ons')
        self.assertEqual(resolve(url).func, add_ons)
