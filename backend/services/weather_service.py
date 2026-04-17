import requests

TOMORROW_API_KEY = "YOUR_API_KEY"

def get_weather_risk(location="Chennai"):
    url = "https://api.tomorrow.io/v4/weather/realtime"

    params = {
        "location": location,
        "apikey": TOMORROW_API_KEY
    }

    try:
        # ✅ ADD timeout HERE (THIS is what I meant)
        res = requests.get(url, params=params, timeout=5).json()

        values = res['data']['values']

        rain = values.get("precipitationIntensity", 0)
        wind = values.get("windSpeed", 0)

        risk = 0

        if rain > 5:
            risk += 50
        if wind > 30:
            risk += 30

        return {
            "rain": rain,
            "wind": wind,
            "risk": risk
        }

    except Exception as e:
        print("Weather API Error:", e)  # 👈 debug log
        return {"rain": 0, "wind": 0, "risk": 0}