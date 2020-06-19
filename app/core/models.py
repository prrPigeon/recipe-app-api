from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


"""
EXTERNAL LINKS

025 Django-manage.py-startapp-docs
https://docs.djangoproject.com/en/2.1/ref/django-admin/#startapp

025 Django-settings-INSTALLED-APPS
https://docs.djangoproject.com/en/2.1/ref/settings/#installed-apps

026 Substituting-a-custom-User-model-in-Django
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-model

026 get-user-model-docs
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.get_user_model

026 check-password-docs
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password

026 CODE-test-models.py
https://gist.github.com/LondonAppDev/2b76e595bd5fba90883ebe4a0a86d436

027 AbstractBaseUser-docs
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser

027 BaseUserManager-docs
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager

027 PermissionsMixin-docs
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.PermissionsMixin

027 CODE-models.py
https://gist.github.com/LondonAppDev/f6d0bf57d6ed4fa21a381ddded67bd34

027 CODE-settings.py
https://gist.github.com/LondonAppDev/765a82921a1739efd276c11dce29a726

028 Django-docs-for-normalize-email-function
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#django.contrib.auth.models.BaseUserManager.normalize_email

028 CODE-test-models.py
https://gist.github.com/LondonAppDev/ede9892a780f3ee9ab20516cc4fb9967

028 CODE-models.py
https://gist.github.com/LondonAppDev/25e5d4674528fdd56415696364b46383

029 CODE-test-models.py
https://gist.github.com/LondonAppDev/af416b2d945d338c2413322cbd50166f

029 CODE-models.py
https://gist.github.com/LondonAppDev/82a12747de0c844d6658949db6517b5a

030 Django-manage.py-createsuperuser-docs
https://docs.djangoproject.com/en/2.1/ref/django-admin/#createsuperuser

030 CODE-test-models.py
https://gist.github.com/LondonAppDev/671e332c5731a8736c60a04038ceb74c

030 CODE-models.py
https://gist.github.com/LondonAppDev/1a9c70be7d3bbe4eca25481ab54a9a8b
"""
