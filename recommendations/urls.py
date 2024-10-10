from django.urls import path
from .views import get_nearby_hotels

urlpatterns = [
    path('nearby-hotels/', get_nearby_hotels, name='nearby_hotels'),
]
