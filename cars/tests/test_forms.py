from django.test import TestCase
# from django.contrib.auth.models import User
from cars.forms import CarRegistrationForm, CarUpdateForm


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
