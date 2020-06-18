from django.test import TestCase
from .models import Car


class CarTests(TestCase):
    """Tests ran against the Car model"""

    def test_str(self):
        test_car_description = Car(year=2020, brand='Ferrari', model='Spider')
        self.assertEqual(str(test_car_description), '2020 Ferrari Spider')
