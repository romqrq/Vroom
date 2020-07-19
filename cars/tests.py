from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from cars.views import all_cars, custom_classic_only, luxury_only, supersport_only, car_register, car_detail, car_edit_view, del_car, add_ons
from cars.forms import CarRegistrationForm, CarUpdateForm
from cars.models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


# class SetupClass(TestCase):
#     """
#     Setting up user, car, track day, insurance and private driver instances
#     """

#     def setUpCar(self):
#         instance = Car.objects.create(
#             car_class='Luxury', price=20, brand='Fiat', model='Panda',
#             year=1992, track_day='Yes', engine_type='Inline 4',
#             displacement=1.2, transmission='Manual', fuel='Petrol',
#             passengers='5', doors=4, accessories='Basic', city="Dublin",
#             county="Dublin", country='Ireland', image1="panda.jpg",
#             guidelines='Guidelines Test'
#         )

# FORMS
class CarRegistrationFormTest(TestCase):
    """Test ran agains Car registration form"""

    def test_CarRegisterForm_valid(self):
        # user = User.objects.create(
        #     username='testuser', first_name='test', last_name='user',
        #     email='tu@test.com', password='123test'
        #     )
        form = CarRegistrationForm(data={
            # 'car_owner': user,
            'car_class': 'Luxury', 'price': 20, 'brand': 'Fiat', 'model': 'Panda',
            'year': 1992, 'track_day': 'Yes', 'engine_type': 'Inline 4',
            'displacement': 1.2, 'transmission': 'Manual', 'fuel': 'Petrol',
            'passengers': '5', 'doors': 4, 'accessories': 'Basic', 'city': "Dublin",
            'county': 'Dublin', 'country': 'Ireland',
            'image1': 'static/images/index/business.jpg',
            'guidelines': 'Guidelines Test'
        })
        print(form)
        self.assertTrue(form.is_valid())

    def test_CarRegisterForm_invalid(self):

        # user = User.objects.create(
        #     username='testuser', first_name='test', last_name='user',
        #     email='tu@test.com', password='123test'
        #     )
        form = CarRegistrationForm(data={
            # 'car_owner': user,
            'car_class': '', 'price': 20, 'brand': '', 'model': 'Panda',
            'year': 1992, 'track_day': 'Yes', 'engine_type': 'Inline 4',
            'displacement': 1.2, 'transmission': 'Manual', 'fuel': 'Petrol',
            'passengers': '5', 'doors': 4, 'accessories': 'Basic', 'city': "Dublin",
            'county': 'Dublin', 'country': 'Ireland',
            'image1': 'static/images/index/business.jpg',
            'guidelines': 'Guidelines Test'
        })
        self.assertFalse(form.is_valid())


# MODELS
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


# URLS
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
