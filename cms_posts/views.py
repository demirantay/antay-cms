# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

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

    # publish form
    if request.POST.get("make_it_public_form_submit"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        new_post = BlogPost(
            author=current_basic_user_profile, title=title, content=content,
            listing_type="public"
        )
        new_post.save()
        return HttpResponseRedirect("/cms-admin/posts/")

    # save draft form submission
    if request.POST.get("draft_save_form_submit"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        new_post = BlogPost(
            author=current_basic_user_profile, title=title, content=content,
            listing_type="draft"
        )
        new_post.save()
        return HttpResponseRedirect("/cms-admin/posts/")


    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "cms_posts/new_post.html", data)
    

def cms_posts_edit(request, post_id):
    """cms panel posts edit page
    """
    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    # get the current post
    try:
        current_post = BlogPost.objects.get(id=post_id)
    except ObjectDoesNotExist:
        current_post = None

    # edit form
    if request.POST.get("make_it_public_form_submit_edit"):
        new_title = request.POST.get("title")
        new_content = request.POST.get("content")
        current_post.title = new_title
        current_post.content = new_content
        current_post.listing_type = "public"
        current_post.save()
        return HttpResponseRedirect("/cms-admin/posts/")

    # save draft form submission
    if request.POST.get("draft_save_form_submit_edit"):
        new_title = request.POST.get("title")
        new_content = request.POST.get("content")
        current_post.title = new_title
        current_post.content = new_content
        current_post.listing_type = "draft"
        current_post.save()
        return HttpResponseRedirect("/cms-admin/posts/")

    data = {
        'current_basic_user': current_basic_user,
        'current_basic_user_profile': current_basic_user_profile,
        'current_post': current_post,
    }
    if current_basic_user == None:
        return HttpResponseRedirect("/auth/login/")
    else:
        return render(request, "cms_posts/edit_post.html", data)
    
    

def blog_single_view(request, post_id):
    """blog post single view
    """
    # get current blog post
    try:
        current_post = BlogPost.objects.get(id=post_id)
    except ObjectDoesNotExist:
        current_post = None

    post_in_draft = False
    if current_post.listing_type == "draft":
        post_in_draft = True
        return HttpResponseRedirect("/cms-admin/posts/")

    data = {
        "current_post": current_post,
        "post_in_draft": post_in_draft,
    }
    return render(request, "cms_posts/blog_single_view.html", data)


@csrf_exempt
def save_draft(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        user = request.user

        draft, created = BlogPost.objects.get_or_create(user=user, defaults={'title': title, 'content': content})
        if not created:
            draft.title = title
            draft.content = content
            draft.last_saved = timezone.now()
            draft.save()

        return JsonResponse({'status': 'success', 'last_saved': draft.last_saved})

    return JsonResponse({'status': 'failed', 'message': 'Invalid request method'})