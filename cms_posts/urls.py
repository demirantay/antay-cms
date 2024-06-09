from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("cms-admin/posts/", views.cms_posts_landing, name="cms_posts_landing"),
    
    # api calls
]