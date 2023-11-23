from django.urls import path

from account.views import signUp, RegisterUserAPIView, login
from hotel.views import get_or_create, get_or_update_or_delete

urlpatterns = [
    path('hotel', get_or_create),
    path('hotel/<str:pk>', get_or_update_or_delete),
]
