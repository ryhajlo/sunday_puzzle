#!/usr/bin/env python
import urllib.request
import sys

data = ""
with urllib.request.urlopen('https://gist.githubusercontent.com/Miserlou/11500b2345d3fe850c92/raw/e36859a9eef58c231865429ade1c142a2b75f16e/gistfile1.txt') as f:
	data = f.read().decode('utf-8')

if not data:
	print("No data read from URL, closing")
	sys.exit()

data = data.split('\n')

#list of dictionaries of cities
RANK = "rank"
CITY = "city"
STATE = "state"
POPULATION = "population"
cities = []

for line in data:
	#only take lines that have text
	if line:
		column_data = line.split(',')
		#check for the right number of columns
		if len(column_data) == 5:
			#check that the first column is the rank
			if column_data[0].isnumeric():
				cities.append({RANK:column_data[0], CITY:column_data[1], STATE:column_data[2], POPULATION:column_data[3]})

print("Found " + str(len(cities)) + " cities")
for city in cities:
	print(city[CITY])
