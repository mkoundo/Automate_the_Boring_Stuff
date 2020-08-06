#! python3
# getopenweather.py
# Author: Michael Koundouros
"""
This program retrieves weather data from OpenWeatherMap.org.
The program does the following:

1. Reads the requested location from the command line
2. Downloads JSON weather data from OpenWeatherMap.org
3. Converts the string of JSON data to a Python data structure
4. Prints the weather for today and the next two days

usage: python getopenweather.py city_name, 2-letter_country_code

e.g. python getopenweather.py London, UK
"""


import sys
import requests
import json


def weather(location, appid):
    # Function retrieves weather data from OpenWeatherMap.org using the appid given

    # Download the JSON data from OpenWeatherMap.org's API.

    # The 7 day forecast api only accepts long/lat and not location name.
    # Therefore, call the current weather api and extract the long/lat coordinates and then call the 7-day api
    # Call current weather api
    # Current weather api info at https://openweathermap.org/current
    current_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={appid}'
    response = requests.get(current_url)
    response.raise_for_status()
    loc_data = json.loads(response.text)
    long = loc_data['coord']['lon']
    lat = loc_data['coord']['lat']

    # Call OneCall api, which contains a 7-day forecast
    # Onecall api info at https://openweathermap.org/api/one-call-api
    seven_day_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={appid}'
    response = requests.get(seven_day_url)
    response.raise_for_status()
    weather_data = json.loads(response.text)
    w = weather_data['daily']

    # Extract and print weather data
    print(f'Current weather in {location}:')
    print(f"{w[0]['weather'][0]['main']} - {w[0]['weather'][0]['description']}")
    print()
    print('Tomorrow:')
    print(f"{w[1]['weather'][0]['main']} - {w[1]['weather'][0]['description']}")
    print()
    print('Day after tomorrow:')
    print(f"{w[2]['weather'][0]['main']} - {w[2]['weather'][0]['description']}")

    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) < 2:
        print('usage: python getopenweather.py city_name, 2-letter_country_code')
        sys.exit(1)

    location = ''.join(args)

    appid = '8625489cfa7ecfc86d398bc41396732d'
    weather(location, appid)
    print('Done!')


if __name__ == '__main__':
    main()
