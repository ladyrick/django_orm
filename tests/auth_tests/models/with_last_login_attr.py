from django_orm.contrib.auth.base_user import AbstractBaseUser


class UserWithDisabledLastLoginField(AbstractBaseUser):
    last_login = None
