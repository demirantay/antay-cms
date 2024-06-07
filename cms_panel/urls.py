from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path("cms-admin/dashboard/", views.panel_dashboard, name="panel_dashboard"),
    
    # api calls
]