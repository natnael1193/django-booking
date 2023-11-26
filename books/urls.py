from django.urls import path

from books.views import get_or_create, get_or_update_or_delete

urlpatterns = [
    path('books', get_or_create),
    path('books/<str:pk>', get_or_update_or_delete)
]
