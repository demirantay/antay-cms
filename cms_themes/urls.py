from django.urls import path
from . import views

urlpatterns = [
    # normal views
    path('', views.theme_index, name='theme_index'),
    path('about/', views.theme_about, name='theme_about'),
    
    # api calls

]