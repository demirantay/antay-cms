# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile
from utils.session_utils import get_current_user, get_current_user_profile


def cms_posts_landing(request):
    """cms panel posts landing page
    """
    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # get all posts


    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "cms_posts/posts_landing.html", data)