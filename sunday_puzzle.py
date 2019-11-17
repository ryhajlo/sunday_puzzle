#!/usr/bin/env python
import urllib.request
import sys

def get_consonants(text_string):
	found_consonants = []
	if text_string:
		CONSONANTS = "bcdfghjklmnpqrstvwxyz"
		for x in text_string:
			char = x.lower()
			if char in CONSONANTS:
				found_consonants.append(char)
	#remove duplicates
	return list(set(found_consonants))

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

# Create a list of cities that have the same number of consanants as their state
consonant_cities = []
for city in cities:
	city_consonants = get_consonants(city[CITY])
	state_consonants = get_consonants(city[STATE])

	#First order check, which cities have the same consonants as their state
	if len(city_consonants) == len(state_consonants):
		#Take the intersection of both
		intersection = list(set(city_consonants).intersection(state_consonants))

		#if the intersection is the same size as either previous list, they are the same
		if len(intersection) == len(city_consonants):
			consonant_cities.append(city)

#Sort by population
consonant_cities = sorted(consonant_cities, key = lambda i: i[POPULATION], reverse = True) 

#Print city information with their associated consonants
for city in consonant_cities:
	print(city[CITY] + ", " + city[STATE] + " population: " + city[POPULATION] + ":")
	for consonant in city_consonants:
		print('\t' + consonant)
