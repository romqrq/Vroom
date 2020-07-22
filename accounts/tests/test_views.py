from django.test import Client, RequestFactory, TestCase
from django.contrib.auth.models import User


class RegisterViewTests(TestCase):
    """
    Tests for user registration view
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

        response = user.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_view_logged_in_redirect(self):
        """Test if logged in usr is redirected to index"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/accounts/register/')

        self.assertEqual(response.url, '/')
        self.assertEqual(response.status_code, 302)


class ProfileViewTests(TestCase):
    """
    Tests for user Profile view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', email='ts@test.com', password="testpass"
        )

    def test_view_not_logged_in_redirect(self):
        """Test if user is redirected when not logged in"""

        user = Client()

        response = user.get('/accounts/profile/')

        self.assertEqual(
            response.url,
            '/accounts/login/?next=/accounts/profile/'
            )
        self.assertEqual(response.status_code, 302)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/accounts/profile/')

        self.assertEqual(response.status_code, 200)


class EditProfileViewTests(TestCase):
    """
    Tests for user Edit Profile view
    """

    def setUp(self):
        """ Creates instance of user in test database """
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            id=99, username='testuser', email='ts@test.com',
            password="testpass"
        )

    def test_view_not_logged_in_redirect(self):
        """Test if user is redirected when not logged in"""

        user = Client()

        response = user.get('/accounts/edit_profile/99')

        self.assertEqual(
            response.url,
            '/accounts/login/?next=/accounts/edit_profile/99'
            )
        self.assertEqual(response.status_code, 302)

    def test_view_logged_in(self):
        """Test if logged in user can access the page"""

        user = Client()
        user.login(username='testuser', password='testpass')

        response = user.get('/accounts/edit_profile/99')

        self.assertEqual(response.status_code, 200)
