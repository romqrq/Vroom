from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from accounts.views import register, profile, edit_user_view, del_user, visit_profile, login, logout
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm, EditUserPasswordForm


class UserRegistrationFormTest(TestCase):
    """Test run against user registration form"""

    def test_UserRegistrationForm_valid(self):
        # user = User.objects.create(
        #     username='testuser', first_name='test', last_name='user',
        #     email='tu@test.com', password1='123test', password2='123test'
        #     )
        form = UserRegistrationForm(data={
            'username': 'testuser', 'first_name': 'test', 'last_name': 'user',
            'email': 'tu@test.com', 'password1': '123test',
            'password2': '123test'
            })
        # form = UserRegistrationForm(instance=user)
        self.assertTrue(form.is_valid())


# URLS
class TestAccountsUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_edit_user_view_url_is_resolved(self):
        url = reverse('edit_user', kwargs={'user_id': 2})
        self.assertEqual(resolve(url).func, edit_user_view)

    def test_delete_user_url_is_resolved(self):
        url = reverse('delete_user', kwargs={'user_id': 2})
        self.assertEqual(resolve(url).func, del_user)

    def test_visit_profile_is_resolved(self):
        url = reverse('visit_profile', kwargs={'user_id': 2})
        self.assertEqual(resolve(url).func, visit_profile)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)
