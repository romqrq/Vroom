from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User


class CartViewTests(TestCase):
    """
    Tests for cart view
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

        response = user.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/cart/')

        self.assertEqual(response.status_code, 200)
