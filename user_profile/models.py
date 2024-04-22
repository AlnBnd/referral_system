from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.base_user import BaseUserManager



# class User(AbstractUser):
#     phone_number = models.CharField(max_length=15, unique=True)
#     verification_code = models.CharField(max_length=4, blank=True)
#     is_verified = models.BooleanField(default=False)
#     invite_code = models.CharField(max_length=6, blank=True, null=True)
#     invite_code_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='referrals')


#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

class UserProfile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=4, blank=True)
    is_verified = models.BooleanField(default=False)
    invite_code = models.CharField(max_length=6, blank=True, null=True)
    activated_invite_code = models.CharField(max_length=6, blank=True, null=True)
    is_activate = models.BooleanField(default=False)
