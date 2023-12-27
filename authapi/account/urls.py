"""
Account Managing Api's
"""


from django.urls import path, include
from account import views


urlpatterns = [

    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),

    path('login/', views.UserLoginView.as_view(), name='user-login')

]
