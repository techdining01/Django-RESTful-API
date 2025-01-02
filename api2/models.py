from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# class CustomUserManager(BaseUserManager):

#     def create_user(self, first_name, last_name, email, password, **extra_fields):
#         if first_name == None:
#             raise ValueError(_('FirstName is required'))
#         if last_name == None:
#             raise ValueError(_('LastName is required'))
#         if email == None:
#             raise ValueError(_('email is required'))
#         if password == None:
#             raise ValueError(_('password is required'))
        
#         email = self.normalize_email(email)

#         user = self.model(first_name,last_name,email,**extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, first_name, last_name, email, password, **extra_fields):

#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
    
#         return self.create_user(first_name, last_name, email, password, **extra_fields)
        

# class CustomUser(AbstractBaseUser, PermissionsMixin):

#     id = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
#     first_name = models.CharField(max_length=255, blank=False, null=False)
#     last_name = models.CharField(max_length=255, blank=False, null=False)
#     email = models.EmailField(unique=True, blank=False, null=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
    

#     USERNAME_FIELD = 'email' 
#     REQUIRED_FIELDS = ['id','first_name', 'last_name']   

#     objects = CustomUserManager()


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