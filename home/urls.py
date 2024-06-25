from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("404/", views.index, name="index"),
    
    # api calls
]