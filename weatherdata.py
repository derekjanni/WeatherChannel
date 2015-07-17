__author__ = 'derekjanni'
import requests
import sqlite3
import re
from bs4 import BeautifulSoup

def clean_numeric(s):
    return int(re.sub("[^0-9]", "", s))

def get(city, state):
    """Scrape Weather.gov for lat, long & temp values"""

    points = get_geo(city, state)
    weather = []
    for latitude, longitude in points:
        try:
            url = 'http://forecast.weather.gov/MapClick.php?lat='+str(latitude)+'&lon='+str(longitude)
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html5lib')
            line = [latitude, longitude, clean_numeric(soup.find(class_='myforecast-current-lrg').text)]
            weather.append(line)
        except:
            pass

    return weather

def get_geo(city, state):
    """Return Lat/Long Coordinates of a given City, ST combo"""
    conn = sqlite3.connect('zipdb.db')
    c = conn.cursor()
    res = c.execute('SELECT DISTINCT Lat, Long FROM zipcodes WHERE CITY=? AND State=?', (city, state)).fetchall()
    conn.commit()
    conn.close()
    return res


#print(get('PORTLAND', 'OR'))