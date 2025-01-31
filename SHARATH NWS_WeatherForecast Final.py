# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h9TUNlgyX8m50ihzA5--orlY5nsjGQsA
"""

#Name SHARATH KUMAR M
#Creation date- 07/04/2021
#version - Python3.6

# import required libraries
import requests
from bs4 import BeautifulSoup

# Create an empty list to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
##try and catch block to check for valid input, if valid input is not provided then exit the script
try:
	lat = float(input('Please input Latitude degrees\n'))
	lon = float(input('Please input Longitude degrees\n'))
except:
	print('Longitude and latitude should be numeric(float)')
	print('Exiting')
	exit()
#before creating url, changing lat nad lon to string datatype
lat=str(lat)
lon=str(lon)
# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text.strip()
    forecast.append(i)



# Print list to remove unicode characters
for day in forecast:
    day = day.replace('\n',': ')
    fday=day.split(':')[0]+': '
    middle=day.split(':')[1].strip()
    mday=[middle[0]]
    for d in middle[1:]:
    	if(d.isupper()):
    		mday.append(' ')
    		mday.append(d)
    	else:
    		mday.append(d)
    middle=''.join(mday)
    last=day.split(':')[-1]
    # add your code here
    day=fday+middle+last
    day=day.replace(' High',', High:')
    day=day.replace(' Low',', Low:')
    day=day.replace('Afternoon',' Afternoon')
    day=day.replace('Night',' Night')
    print(day.strip().upper())
