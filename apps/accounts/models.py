from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email,password, role='admin',is_staff=True,is_superuser=True)
    


class User(AbstractUser, PermissionsMixin):
    ROLE_CHOSES =(
        ('customer', 'Customer'),
        ('admin', 'Admin'),
        ('seller', 'Seller'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOSES, default='customer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email
    

