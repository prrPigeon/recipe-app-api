from django.test import TestCase
# get_user_model je helper funkcija,
# pametnije je da se importuje ona, a ne User
# kasnije se samo u settingsu zameni itd.
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """ Test creating a new user with email is successful"""
        email = "test@belgrade.com"
        password = "test123435"
        user = get_user_model().objects.create_user(
             email=email,
             password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@BELGRADE.COM'
        user = get_user_model().objects.create_user(
            email, 'test12345'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test12345'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@belgrade.com',
            'test12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

# Comand for testing:
# docker-compose run app sh -c "python manage.py test"
