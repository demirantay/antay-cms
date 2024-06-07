# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from .models import BasicUserProfile

from utils.auth_utils import get_banned_words
from utils.session_utils import get_current_user, get_current_user_profile


def login_page(request):
    """
    Login page where the users can login to the site
    """
    # admin user session pop
    # admin user session pop
    # Deleting any sessions regarding top-tier type of users

    # Deleting sessions regarding basic users
    if "basic_user_email" in request.session:
        del request.session["basic_user_email"]
        del request.session["basic_user_username"]
        del request.session["basic_user_logged_in"]

    # Login Form Processing
    invalid_credentials = False

    if request.POST.get("login_form_submit_btn"):
        username = request.POST.get("username")
        password = request.POST.get("password")

         # checking if the inputs are empty
        if bool(username) == False or bool(password) == False:
            invalid_credentials = True
        else:
            # Check if the user credits are right and if they
            # are log the user into the system and add sessions
            try:
                user = User.objects.get(username=username)
            except ObjectDoesNotExist:
                user = None

            if user == None:
                invalid_credentials = True
            else:
                # check password if it matches
                # redirect to home with sessions
                is_valid = user.check_password(password)
                if is_valid == True:
                    # update user info sessions
                    request.session["basic_user_email"] = user.email
                    request.session["basic_user_username"] = user.username
                    request.session["basic_user_logged_in"] = True
                    return HttpResponseRedirect("/progress/")
                else:
                    invalid_credentials = True

    # Preventing brute force
    # ... havent implemented this yet

    data = {
         "invalid_credentials": invalid_credentials,
    }
    return render(request, "authentication/login.html", data)


def logout(request):
    """
    if users visit this page it logs her out.
    """
    # Deleting sessions regarding basic users
    if "basic_user_email" in request.session:
        del request.session["basic_user_email"]
        del request.session["basic_user_username"]
        del request.session["basic_user_logged_in"]

    return HttpResponseRedirect("/")


def dashboard(request):
    """this is the main dashboard page when you enter the panel
    """
    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "authentication/dashboard.html", data)