from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User

class CheckoutViewTests(TestCase):
    """
    Tests for checkout view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in_redirect(self):
        """Test if user is redirected to login page when not logged in"""

        user = Client()

        response = user.get('/checkout/')

        self.assertEqual(
            response.url,
            '/accounts/login/?next=/checkout/'
            )
        self.assertEqual(response.status_code, 302)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/checkout/')

        self.assertEqual(response.status_code, 200)
