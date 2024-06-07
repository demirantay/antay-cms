from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("auth/login/", views.login_page, name="login_page"),
    path("auth/logout/", views.logout, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),
    
    # api calls
]