USE_ROUNDED_COORDS = True
OPENWEATHER_API = "0254bcf2c9ada8933ad29c7a401f30b1" # You can create an API key at openweathermap.org, it is easy and Free
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=en&"
    "units=metric"
)
