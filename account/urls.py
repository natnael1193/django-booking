from django.urls import path

from account.views import signUp, RegisterUserAPIView, login

urlpatterns = [
    path('signup/', signUp),
    path('login/', login),
    path('register/', RegisterUserAPIView.as_view())
]
