from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User


class IndexViewTests(TestCase):
    """
    Tests for index view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_int(self):
        """Test if user can access the page when not logged in"""

        user = Client()

        response = user.get('/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/')

        self.assertEqual(response.status_code, 200)


class AboutViewTests(TestCase):
    """
    Tests for about view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access page when not logged in"""

        user = Client()

        response = user.get('/home/about/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/home/about/')

        self.assertEqual(response.status_code, 200)


class FAQsViewTests(TestCase):
    """
    Tests for FAQs view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access page when not logged in"""

        user = Client()

        response = user.get('/home/FAQs/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/home/FAQs/')

        self.assertEqual(response.status_code, 200)


class ContactViewTests(TestCase):
    """
    Tests for contact view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in(self):
        """Test if user can access page when not logged in"""

        user = Client()

        response = user.get('/home/contact/')

        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/home/contact/')

        self.assertEqual(response.status_code, 200)
