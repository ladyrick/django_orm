from django_orm.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_orm.db import models


class IsActiveTestUser1(AbstractBaseUser):
    """
    This test user class and derivatives test the default is_active behavior
    """

    username = models.CharField(max_length=30, unique=True)

    custom_objects = BaseUserManager()

    USERNAME_FIELD = "username"

    # the is_active attr is provided by AbstractBaseUser
