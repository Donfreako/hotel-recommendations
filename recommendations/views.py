import requests
from django.http import JsonResponse
from django.conf import settings

def get_nearby_hotels(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    api_key = settings.GOOGLE_API_KEY

    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f"{latitude},{longitude}",
        'radius': 5000,  # Search within a 5 km radius
        'type': 'lodging',  # Use 'lodging' for hotels
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        hotels = response.json().get('results', [])
        sorted_hotels = sorted(hotels, key=lambda x: x.get('rating', 0), reverse=True)

        hotel_list = [
            {
                'name': hotel.get('name'),
                'rating': hotel.get('rating'),
                'address': hotel.get('vicinity')
            }
            for hotel in sorted_hotels
        ]

        return JsonResponse({'hotels': hotel_list})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
