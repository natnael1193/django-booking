from django.urls import path

from room_quantity.views import get_or_create, get_or_update_or_delete

urlpatterns = [
    path('room_quantity/', get_or_create),
    path('room_quantity/<str:pk>', get_or_update_or_delete),
]
