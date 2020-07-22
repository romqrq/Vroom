from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User
from cars.models import Car


class AllCarsViewTests(TestCase):
    """
    Tests for all cars view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access the page when not logged in"""

        user = Client()

        response = user.get('/cars/')
        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/')

        self.assertEqual(response.status_code, 200)

        # response = user.get('/accounts/register/')

        # self.assertEqual(response.url, '/')
        # self.assertEqual(response.status_code, 302)


class CustomClassicViewTests(TestCase):
    """
    Tests for custom classic cars view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access the page when not logged in"""

        user = Client()

        response = user.get('/cars/custom_classic/')
        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/custom_classic/')

        self.assertEqual(response.status_code, 200)


class LuxuryViewTests(TestCase):
    """
    Tests for luxury cars view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access the page when not logged in"""

        user = Client()

        response = user.get('/cars/luxury/')
        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/luxury/')

        self.assertEqual(response.status_code, 200)


class SupersportViewTests(TestCase):
    """
    Tests for supersport cars view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access the page when not logged in"""

        user = Client()

        response = user.get('/cars/supersport/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/supersport/')

        self.assertEqual(response.status_code, 200)


class RentMyCarViewTests(TestCase):
    """
    Tests for user car registration/rent my car view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """
        Test if user can't access the page when not logged in
        and is redirected to login page
        """

        user = Client()

        response = user.get('/cars/rent_my_car/')

        self.assertEqual(response.url, '/accounts/login/?next=/cars/rent_my_car/')
        self.assertEqual(response.status_code, 302)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/rent_my_car/')

        self.assertEqual(response.status_code, 200)


class CarDetailViewTests(TestCase):
    """
    Tests for car details view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )
        self.car = Car.objects.create(
            car_class='Luxury', price=20, brand='Fiat', model='Panda',
            year=1992, track_day='Yes', engine_type='Inline 4',
            displacement=1.2, transmission='Manual', fuel='Petrol',
            passengers=5, doors=4, accessories='Basic', city="Dublin",
            county="Dublin", country='Ireland',
            image1="Vroom/static/images/index/business.jpg",
            guidelines='Guidelines Test'
        )
    # SAME PROBLEM FOR EDIT AND DELETE
    # def test_view_not_logged_in(self):
    #     """
    #     Test if user can access the page when not logged in
    #     """

    #     user = Client()

    #     response = user.get('/cars/car_details/', kwargs={'car_id': 1})

    #     self.assertEqual(response.status_code, 200)

    # def test_view_logged_in(self):
    #     """Test if logged in user can access the page"""

    #     user = Client()
    #     user.login(username='testuser', password='testpass')

    #     response = user.get('/cars/car_details/', kwargs={'car_id': 1})

    #     self.assertEqual(response.status_code, 200)


class AddonsViewTests(TestCase):
    """
    Tests for addons view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """
        Test if user can access the page when not logged in
        """

        user = Client()

        response = user.get('/cars/add_ons/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cars/add_ons/')

        self.assertEqual(response.status_code, 200)