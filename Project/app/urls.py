from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserDataView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('userdata/', UserDataView.as_view()),
]