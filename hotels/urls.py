from django.urls import path
from .views import get_nearby_hotels, hotel_search_form

urlpatterns = [
    path('search_form/', hotel_search_form, name='hotel_search_form'),
    path('search_hotels/', get_nearby_hotels, name='search_hotels'),
]
