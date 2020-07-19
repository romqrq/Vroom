from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import register, profile, edit_user_view, del_user, visit_profile, login, logout


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
