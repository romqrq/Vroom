from django.test import TestCase
from .models import Car


class CarTests(TestCase):
    """Tests ran against the Car model"""

    def test_str(self):
        test_brand = Car(brand='Ferrari')
        self.assertEqual(str(test_brand), 'Ferrari')
