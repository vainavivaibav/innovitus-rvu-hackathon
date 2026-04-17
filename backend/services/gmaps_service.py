import requests

GOOGLE_MAPS_API_KEY = "YOUR_API_KEY"

def get_route_data(origin="Chennai", destination="Bangalore"):
    url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": origin,
        "destination": destination,
        "departure_time": "now",
        "traffic_model": "pessimistic",
        "key": GOOGLE_MAPS_API_KEY
    }

    try:
        # ✅ Safe API call with timeout
        res = requests.get(url, params=params, timeout=5).json()

        # ✅ Validate response before accessing
        if "routes" not in res or len(res["routes"]) == 0:
            return {
                "distance": "N/A",
                "duration": "N/A",
                "traffic_time": "N/A"
            }

        route = res['routes'][0]['legs'][0]

        return {
            "distance": route['distance']['text'],
            "duration": route['duration']['text'],
            "traffic_time": route.get('duration_in_traffic', {}).get('text', "N/A")
        }

    except Exception as e:
        print("Google Maps API Error:", e)  
        return {
            "distance": "N/A",
            "duration": "N/A",
            "traffic_time": "N/A"
        }