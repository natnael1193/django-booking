from django.urls import path

from room.views import get_or_create, get_or_update_or_delete

urlpatterns = [
    path('rooms', get_or_create),
    path('rooms/<str:pk>', get_or_update_or_delete),
]
