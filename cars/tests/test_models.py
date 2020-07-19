from django.test import TestCase
# from django.contrib.auth.models import User
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


class CarTests(TestCase):
    """Tests ran against the Car model"""

    def test_str(self):
        test_car_description = Car(year=2020, brand='Ferrari', model='Spider')
        self.assertEqual(str(test_car_description), '2020 Ferrari Spider')

    def test_fail_str(self):
        test_car_description = Car(year=2020, brand='', model='Spider')
        self.assertNotEqual(str(test_car_description), '2020 Ferrari Spider')

    def test_full_car(self):
        car = Car.objects.create(
            car_class='Luxury', price=20, brand='Fiat', model='Panda',
            year=1992, track_day='Yes', engine_type='Inline 4',
            displacement=1.2, transmission='Manual', fuel='Petrol',
            passengers=5, doors=4, accessories='Basic', city="Dublin",
            county="Dublin", country='Ireland', image1="panda.jpg",
            guidelines='Guidelines Test'
        )
        with self.subTest():
            self.assertEqual(car.car_class, 'Luxury')
        with self.subTest():
            self.assertEqual(car.price, 20)
        with self.subTest():
            self.assertEqual(car.brand, 'Fiat')
        with self.subTest():
            self.assertEqual(car.model, 'Panda')
        with self.subTest():
            self.assertEqual(car.year, 1992)
        with self.subTest():
            self.assertEqual(car.track_day, 'Yes')
        with self.subTest():
            self.assertEqual(car.engine_type, 'Inline 4')
        with self.subTest():
            self.assertEqual(car.displacement, 1.2)
        with self.subTest():
            self.assertEqual(car.transmission, 'Manual')
        with self.subTest():
            self.assertEqual(car.fuel, 'Petrol')
        with self.subTest():
            self.assertEqual(car.passengers, 5)
        with self.subTest():
            self.assertEqual(car.doors, 4)
        with self.subTest():
            self.assertEqual(car.accessories, 'Basic')
        with self.subTest():
            self.assertEqual(car.city, 'Dublin')
        with self.subTest():
            self.assertEqual(car.county, 'Dublin')
        with self.subTest():
            self.assertEqual(car.country, 'Ireland')
        with self.subTest():
            self.assertEqual(car.image1, "panda.jpg")
        with self.subTest():
            self.assertEqual(car.guidelines, 'Guidelines Test')


class TrackDayTests(TestCase):
    """Tests ran against the Track Day addon model"""

    def test_str(self):
        test_track_description = TrackDayAddon(coverage='Morning')
        self.assertEqual(str(test_track_description), 'Track Day Morning')

    def test_fail_str(self):
        test_track_description = TrackDayAddon(coverage='Afternoon')
        self.assertNotEqual(str(test_track_description), 'Track Day Morning')

    def test_full_track(self):
        track = TrackDayAddon.objects.create(
            coverage='Morning', price=120, description='Track Description',
            image='track.jpg'
        )
        with self.subTest():
            self.assertEqual(track.title, 'Track Day')
        with self.subTest():
            self.assertEqual(track.coverage, 'Morning')
        with self.subTest():
            self.assertEqual(track.price, 120)
        with self.subTest():
            self.assertEqual(track.description, 'Track Description')
        with self.subTest():
            self.assertEqual(track.image, 'track.jpg')


class InsuranceTests(TestCase):
    """Tests ran against the Insurance addon model"""

    def test_str(self):
        insurance_description = InsuranceAddon(coverage='Full Coverage')
        self.assertEqual(str(insurance_description), 'Insurance Full Coverage')

    def test_fail_str(self):
        insurance_description = InsuranceAddon(coverage='Basic')
        self.assertNotEqual(str(insurance_description),
                            'Insurance Full Coverage')

    def test_full_insurance(self):
        insurance = InsuranceAddon.objects.create(
            coverage='Basic', price=120, description='Insurance Description',
            image='insurance.jpg'
        )
        with self.subTest():
            self.assertEqual(insurance.title, 'Insurance')
        with self.subTest():
            self.assertEqual(insurance.coverage, 'Basic')
        with self.subTest():
            self.assertEqual(insurance.price, 120)
        with self.subTest():
            self.assertEqual(insurance.description, 'Insurance Description')
        with self.subTest():
            self.assertEqual(insurance.image, 'insurance.jpg')


class PrivateDriverTests(TestCase):
    """Tests ran against the Insurance addon model"""

    def test_str(self):
        private_driver_description = PrivateDriverAddon(coverage='Yes')
        self.assertEqual(str(private_driver_description), 'Private Driver Yes')

    def test_fail_str(self):
        private_driver_description = PrivateDriverAddon(coverage='Yes')
        self.assertNotEqual(str(private_driver_description), 'Private Driver')

    def test_full_driver(self):
        driver = PrivateDriverAddon.objects.create(
            coverage='Yes', price=300, description='Driver Description',
            image='driver.jpg'
        )
        with self.subTest():
            self.assertEqual(driver.title, 'Private Driver')
        with self.subTest():
            self.assertEqual(driver.coverage, 'Yes')
        with self.subTest():
            self.assertEqual(driver.price, 300)
        with self.subTest():
            self.assertEqual(driver.description, 'Driver Description')
        with self.subTest():
            self.assertEqual(driver.image, 'driver.jpg')
