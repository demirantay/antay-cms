# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from .models import BlogPost
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
    try:
        all_posts = BlogPost.objects.all().order_by("-id")
    except ObjectDoesNotExist:
        all_posts = None

    # post delete form processing
    if request.POST.get("delete_single_post"):
        hidden_id = request.POST.get("hidden_id")
        targeted_post = BlogPost.objects.get(id=hidden_id)
        targeted_post.delete()
        return HttpResponseRedirect("/cms-admin/posts/")

    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
        'all_posts': all_posts,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "cms_posts/posts_landing.html", data)
    


def cms_posts_create(request):
    """cms panel posts create page
    """
    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # create new post form submission

    # save draft form submission


    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "cms_posts/new_post.html", data)
    

def blog_single_view(request, post_id):
    """blog post single view
    """
    # get current blog post
    try:
        current_post = BlogPost.objects.get(id=post_id)
    except ObjectDoesNotExist:
        current_post = None

    data = {
        "current_post": current_post,
    }
    return render(request, "cms_posts/blog_single_view.html", data)
