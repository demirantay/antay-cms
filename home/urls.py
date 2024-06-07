from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("", views.index, name="index"),
    
    # api calls
]