from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser , PermissionsMixin)
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('the email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email ,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must be have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must be is_superuser=True')
        return self.create_user(email,password,**extra_fields)

        
class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=250 , unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    objects = UserManager()

    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.ForeignKey(User ,on_delete = models.CASCADE )
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    image = models.ImageField(blank = True,null = True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.user.email
    
@receiver(post_save , sender =User)
def save_profile(sender , instance , created ,**kwargs):
    if created :
        Profile.objects.create(user=instance)