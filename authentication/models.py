# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports


class BasicUserProfile(models.Model):
    """
    Data: About the users that signup to the site
    """
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)

    # O2One relationship with django's user model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Settings -- Edit Profile
    profile_photo = models.ImageField(
        upload_to="profile_photo/", blank=True, null=True
    )
    email = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    linkedin_URL = models.CharField(max_length=200, blank=True, null=True)

    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_URL = models.CharField(max_length=200, blank=True, null=True)
    company_location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "User: " + str(self.user.username)