from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("cms-admin/posts/", views.cms_posts_landing, name="cms_posts_landing"),
    path("cms-admin/posts/create/", views.cms_posts_create, name="cms_posts_create"),
    path("cms-admin/post/edit/<int:post_id>", views.cms_posts_edit, name="cms_posts_edit"),

    path("blog/<int:post_id>/", views.blog_single_view, name="blog_single_view"),
    
    # api calls
    path('api/save-draft/', views.save_draft, name='save_draft'),
]