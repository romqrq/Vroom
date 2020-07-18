from django.test import TestCase, Client
# from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .forms import CarRegistrationForm, CarUpdateForm
from .models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


class SetupClass(TestCase):
    """
    Setting up user, car, track day, insurance and private driver instances
    """

    def setUpCar(self):
        instance = Car.objects.create(
            car_class='Luxury', price=20, brand='Fiat', model='Panda',
            year=1992, track_day='Yes', engine_type='Inline 4',
            displacement=1.2, transmission='Manual', fuel='Petrol',
            passengers='5', doors=4, accessories='Basic', city="Dublin",
            county="Dublin", country='Ireland', image1="panda.jpg",
            guidelines='Guidelines Test'
        )

class CarRegistrationFormTest(TestCase):
    """Test ran agains Car registration form"""

    # override settings for media dir
    # @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    # def setUpUser(self):
    #     self.user = User.objects.create(
    #         username='testuser', first_name='test', last_name='user',
    #         email='tu@test.com', password='123test'
    #     )

    # data={
    #         'car_owner': user,
    #         'car_class': 'Luxury', 'price': 20, 'brand': 'Fiat',
    #         'model': 'Panda', 'year': 1992, 'track_day': 'Yes',
    #         'engine_type': 'Inline 4', 'displacement': 1.2,
    #         'transmission': 'Manual', 'fuel': 'Petrol', 'passengers': '5',
    #         'doors': 4, 'accessories': 'Basic', 'city': "Dublin",
    #         'county': "Dublin", 'country': 'Ireland',
    #         'image1': 'static/images/index/business.jpg',
    #         'guidelines': 'Guidelines Test'
    #     }
    def test_CarRegisterForm_valid(self):
        user = User.objects.create(
            username='testuser', first_name='test', last_name='user',
            email='tu@test.com', password='123test'
            )
        car = Car.objects.create(
            car_owner=user,
            car_class='Luxury', price=20, brand='Fiat', model='Panda',
            year=1992, track_day='Yes', engine_type='Inline 4',
            displacement=1.2, transmission='Manual', fuel='Petrol',
            passengers='5', doors=4, accessories='Basic', city="Dublin",
            county='Dublin', country='Ireland',
            image1='static/images/index/business.jpg',
            guidelines='Guidelines Test'
        )
        form = CarRegistrationForm(instance=car)
        self.assertTrue(form.is_valid())

    def test_CarRegisterForm_invalid(self):

        user = User.objects.create(
            username='testuser', first_name='test', last_name='user',
            email='tu@test.com', password='123test'
            )
        car = Car.objects.create(
            car_owner=user,
            car_class='Luxury', price=20, brand='Fiat', model='Panda',
            year=1992, track_day='Yes', engine_type='Inline 4',
            displacement=1.2, transmission='Manual', fuel='Petrol',
            passengers='5', doors=4, accessories='Basic', city="Dublin",
            county='Dublin', country='Ireland',
            image1='static/images/index/business.jpg',
            guidelines='Guidelines Test'
        )
        form = CarRegistrationForm(instance=car)
        self.assertFalse(form.is_valid())


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
        self.assertNotEqual(str(insurance_description), 'Insurance Full Coverage')

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
