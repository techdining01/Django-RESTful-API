from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# class UserManager(BaseUserManager):

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_('You must provide email'))
#         email = self.normalize_email(email)
#         user = self.model(email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_user(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)


#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.PositiveIntegerField(primary_key=True, null=False, blank=False,unique=True)
#     email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
#     username = models.CharField(max_length=255, null=False, blank=False)
#     password = models.CharField(max_length=255, null=False, blank=False)

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = UserManager()
    
#     def __str__(self):
#         return self.username
    
#     def get_full_name(self):
#         return self.username
    
#     def get_short_name(self):
#         return self.username or self.email.split('@')[0]
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name,password=None, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name, last_name=last_name,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, first_name,last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name,last_name, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.first_name
    
    def get_full_name(self):
        return self.first_name
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

