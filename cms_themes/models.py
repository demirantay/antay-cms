# Main Imports

# Django Imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# My Module Imports
from authentication.models import BasicUserProfile


class WebsiteTheme(models.Model):
    """Current Theme that the User selected"""
    id = models.AutoField(primary_key=True)
    creation_date = models.DateField(default=timezone.now)
    theme_name = models.CharField(max_length=1000)

    def __str__(self):
        return "Current Theme: " + self.theme_name