import json
from typing import TypedDict
from datetime import datetime
from pathlib import Path
from weather_api_service import Weather
from weather_formatter import format_weather
from typing import Protocol



class WeatherStorage(Protocol):
    """Interface for any storage saving weather"""
    def save(self, weather: Weather) -> None:
        raise NotImplementedError

class HistoryRecord(TypedDict):
    date: str
    weather: str
    temperature: str
    city: str
    sunrise: str
    sunset: str

class JSONFileWeatherStorage:
    """Store weather in JSON file"""
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": weather.weather_type,
            "temperature": str(weather.temperature),
            "city": weather.city,
            "sunrise": str(weather.sunrise),
            "sunset": str(weather.sunset)
        })
        self._write(history)
    
    def _init_storage(self) -> None:
        if not self._jsonfile.exists():
            self._jsonfile.write_text("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the storage"""
    storage.save(weather)