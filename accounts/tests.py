from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, EditUserForm, EditUserPasswordForm


class UserRegistrationFormTest(TestCase):
    """Test run against user registration form"""

    def test_UserRegistrationForm_valid(self):
        user = User.objects.create(
            username='testuser', first_name='test', last_name='user',
            email='tu@test.com', password='123test'
            )
        form = UserRegistrationForm(instance=user)
        self.assertTrue(form.is_valid())
