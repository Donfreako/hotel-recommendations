from django.shortcuts import render
import requests

def get_nearby_hotels(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    if latitude and longitude:
        overpass_url = "http://overpass-api.de/api/interpreter"
        
        overpass_query = f"""
        [out:json];
        node
          ["tourism"="hotel"]
          (around:5000,{latitude},{longitude});
        out body;
        """

        try:
            response = requests.post(overpass_url, data={'data': overpass_query})
            response.raise_for_status()

            hotels = response.json().get('elements', [])
            result = []
            
            for hotel in hotels:
                name = hotel.get('tags', {}).get('name', 'Unnamed Hotel')
                lat = hotel.get('lat')
                lon = hotel.get('lon')
                stars = hotel.get('tags', {}).get('stars', 'No rating available')
                cuisine = hotel.get('tags', {}).get('cuisine', 'No specific cuisine')

                result.append({
                    'name': name,
                    'latitude': lat,
                    'longitude': lon,
                    'address': f"Lat: {lat}, Lon: {lon}",
                    'rating': stars,
                    'cuisine': cuisine
                })

            return render(request, 'hotels/results.html', {'hotels': result})

        except requests.exceptions.RequestException as e:
            return render(request, 'hotels/results.html', {'error': str(e)})

    return render(request, 'hotels/search_form.html')
def hotel_search_form(request):
    return render(request, 'hotels/search_form.html')
