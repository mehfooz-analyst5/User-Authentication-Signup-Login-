"""
Account Managing Api's
"""


from django.urls import path, include
from account import views


urlpatterns = [

    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),

    path('changepassword/', views.UserChangePasswordView.as_view(), name='user-changpassword'),

]
