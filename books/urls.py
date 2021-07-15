from django.urls import path
from . import controller


urlpatterns = (
    path('', controller.list, name='list'),
    path('book/<int:pk>/', controller.book, name='book'),
)
