from django.urls import path
from .import views

urlpatterns = [
    path('', views.indexHome, name='homepage'),
]