# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# My Module Imports
from .models import WebsiteTheme
from authentication.models import BasicUserProfile


def theme_index(request):
    try:
        current_theme = WebsiteTheme.objects.last()
    except ObjectDoesNotExist:
        current_theme = None
    
    return render(request, f'cms_themes/{current_theme.theme_name}/index.html')


def theme_about(request):
    try:
        current_theme = WebsiteTheme.objects.last()
    except ObjectDoesNotExist:
        current_theme = None
    
    return render(request, f'cms_themes/{current_theme.theme_name}/about.html')