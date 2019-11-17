#!/usr/bin/env python
"""I heard on the radio this morning the following puzzle: Mobile, Alabama has a unique property,
   it has the same consanats in the city name as the state name. Find the city in that has the
   largest population with this property.
   This seems pretty obvious, as it would be New York, New York. However, I wanted to write a
   program to find them all. I found a file that contains the 1000 largest cities in the US,
   and ran the following code."""
import urllib.request

def get_consonants(text_string):
    """Given a string, return a list of unique consonants within that string"""
    found_consonants = []
    if text_string:
        consonants = "bcdfghjklmnpqrstvwxyz"
        for char in text_string.lower():
            if char in consonants:
                found_consonants.append(char)
    #remove duplicates
    return list(set(found_consonants))

RANK = "rank"
CITY = "city"
STATE = "state"
POPULATION = "population"

def get_cities():
    """Get a list of dictionaries for all city information"""

    data = ""
    with urllib.request.urlopen('https://gist.githubusercontent.com/Miserlou/11500b2345d3fe850c92/raw/e36859a9eef58c231865429ade1c142a2b75f16e/gistfile1.txt') as text:
        data = text.read().decode('utf-8')

    if not data:
        print("No data read from URL, closing")
        return []

    data = data.split('\n')

    #list of dictionaries of cities
    cities = []
    for line in data:
        #only take lines that have text
        if line:
            column_data = line.split(',')
            #check for the right number of columns
            if len(column_data) == 5:
                #check that the first column is the rank
                if column_data[0].isnumeric():
                    cities.append({RANK:column_data[0],
                                   CITY:column_data[1],
                                   STATE:column_data[2],
                                   POPULATION:column_data[3]})
    return cities

def get_cities_with_consonants(cities):
    """Given a list of cities, get a list of cities where they have the same consonants as their
       state name"""
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
    return consonant_cities

def main():
    """Main function"""

    #Get a list of all cities
    cities = get_cities()

    #Get a list of cities with matching consonants to their state name
    consonant_cities = get_cities_with_consonants(cities)

    #Sort by population
    consonant_cities = sorted(consonant_cities, key=lambda i: i[POPULATION], reverse=True)

    #Print city information with their associated consonants
    for city in consonant_cities:
        print(city[CITY] + ", " + city[STATE] + " population: " + city[POPULATION] + ":")
        for consonant in get_consonants(city[CITY]):
            print('\t' + consonant)

main()
