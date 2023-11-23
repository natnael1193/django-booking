from django.urls import path

from room_type.views import get_or_create, get_or_update_or_delete

urlpatterns = [
    path('room_type/', get_or_create),
    path('room_type/<str:pk>', get_or_update_or_delete),
]
