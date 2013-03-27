from __future__ import unicode_literals
from random import choice
import requests

# Our API endpoint...
url = 'http://api.brewerydb.com/v2/search'

# Ask the user for what beer we should query for?
query = raw_input('What beer do you want to search for?: ')

# Replace <Your API key> with your own BreweryDB key.
# You can register it here. http://www.brewerydb.com/developers/
params = {
    'key': '<Your API key>',
    'q': query,
    'type': 'beer'
}

# Send a GET request to the end, passing in the params.
response = requests.get(url, params=params)

# Extract the json from the response and turn it into a
# python dictionary.
json = response.json()

# The list of beers is contained it the 'data' key
# Let's store that in a seperate variable.
beers = json['data']

# How many beers?
total_beers = len(beers)
print "Found {} beers".format(total_beers)

# What is the first beer?
first_beer = beers[0]
print "The first beer is {}".format(first_beer['name'])

# What is the last beer?
last_beer = beers[-1]
print "The last beer is {}".format(last_beer['name'])

# Time for something more complex!
# Let's Randomly select a beer!
random_beer = choice(beers)

# Sort the name of the beer is a seperate variable
name = random_beer['name']

# We know try to get the description
try:
    description = random_beer['description']
# But, the API does not always return a description
# So if we can't find one, we use the default below.
except:
    description = 'No description available.'

print "Your randomly selected beer is {}. {}".format(
    name, description)
