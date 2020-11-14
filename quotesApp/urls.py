from django.urls import path
from .import views

urlpatterns = [
    path('user/register/', views.register, name='register'),
    path('user/login/', views.loginUser, name='login'),
    path('user/logout/', views.logout_, name='logout'),
    path('wish/AddWishes/', views.addWishes, name='addWishes'),
    path('user/changePassword/', views.customPasswordChange, name='changePassword'),
    path('user/profile/', views.UserProfile, name='profile')
]