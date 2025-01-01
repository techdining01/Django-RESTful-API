from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(UserManager):

    def create_user(self, username, email, password = None, **extra_fields):
        if username == None:
            raise ValueError(_('UserName must not be Empty'))
        if email == None:
            raise ValueError(_('Email is required'))
        if password == None:
            raise ValueError(_('Password must be set'))
        