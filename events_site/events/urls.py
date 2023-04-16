from django.urls import path
from .views import get_events, get_categories

urlpatterns = [
    path('events/', get_events, name='event-list'),
    path('categories/', get_categories, name='categories-list'),
]
