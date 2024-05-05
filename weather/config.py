USE_ROUNDED_COORDS = True
OPENWEATHER_API = <YOUR_OPENWEATHER_API_KEY> # You can create an API key at openweathermap.org, it is easy and Free
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=en&"
    "units=metric"
)
