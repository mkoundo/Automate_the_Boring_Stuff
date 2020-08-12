#! python3
# umbrella_reminder.py
# Author: Michael Koundouros
"""
Chapter 12 showed you how to use the requests module to scrape data from https://weather.gov/. Write a program
that runs just before you wake up in the morning and checks whether it’s raining that day. If so, have the program
text you a reminder to pack an umbrella before leaving the house.
"""


import bs4
import requests
import ezgmail
import datetime
from threading import Timer

x = datetime.datetime.today()

# Wake-up time at hour = h, minute = mm
y = x.replace(day=x.day, hour=6, minute=30, second=0, microsecond=0) + datetime.timedelta(days=1)
delta_t = y - x

sec = delta_t.total_seconds()


def get_weather():
    # Extract weather data for zip code 94105 from https://weather.gov/
    res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.78907000000004&lon=-122.39492999999999')
    res.raise_for_status()

    site_data = bs4.BeautifulSoup(res.text, 'html.parser')
    forecast = site_data.select('#detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text')
    todays_weather = forecast[0].getText()
    print(todays_weather)

    if todays_weather.find('rain') != -1:
        # Requires email to sms gateway address
        ezgmail.send('legowaj684@mailvk.net', 'Re: Weather', "Rain expected; don't forget your umbrella!")


t = Timer(sec, get_weather)
t.start()


# The program above will only run once at wake-up time. Alternatively use Windows Scheduler to run every morning.
