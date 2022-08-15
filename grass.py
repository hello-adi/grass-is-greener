import os
import requests

OPENWEATHER_URL = (
    "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={}&q=Delhi"
)
OPENWEATHER_API_KEY = ""


def location_coordinate(loc):
    # api call for getting cordinate
    pass


location = input("Enter the location:")

# api call to openweather
# GET api.openweathermap.org KEY "&q='location'"
location_weather = location_coordinate(location)

# return the current weather at user location

# search for a place with opposite weather

# grass isn't always greener.
