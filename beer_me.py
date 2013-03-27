'''
Ask the user to search for a type of beer; choose a randomly matching result.
API documentation available here: http://www.brewerydb.com/developers/docs-endpoint/search_index
'''

from __future__ import unicode_literals # Deal with unicode string characters
from random import choice # Import the ability to randomly choose from a list
import requests # Load functionality from the Requests module


# The 'search' endpoint of the API
url = 'http://api.brewerydb.com/v2/search'

# Let the user type in a search term to use in the query
query = raw_input("What beer do you want to search for? ")

# A dictionary of parameters to be passed into the GET request
#  'type' is an optional parameters but specifies that we want to search for 
#  beer rather than breweries, events, etc.
params = {
    'key': '6208ddfdc0ffb605cc28baee87e4dcd4',
    'q': query,
    'type': 'beer'
}

# Get the API's response from a GET request to the following URL:
# http://api.brewerydb.com/v2/search/?key=6208ddfdc0ffb605cc28baee87e4dcd4&q={query}&type=beer
#  where {query} represents the actual text input by the user
response = requests.get(url, params=params)
json = response.json() # the JSON data from the response, stored as a dictionary

# Get the value corresponding to the 'data' key, which is a list of beers 
beers = json['data'] 
# How many beers? Get the length of the list:
total_beers = len(beers)
# What is the first beer? At index number 0:
first_beer = beers[0]
# What is the last beer? Use negative indexing to look from the right side:
last_beer = beers[-1]
# Randomly select a beer!
random_beer = choice(beers)

# Get the name out of this individual dictionary representing the beer's info
name = random_beer['name']

# Try to get a description out of the beer's info if one is available
try:
    description = random_beer['description']
except:
    description = 'No description available.'

# Display the beer's name and description
print "Your randomly selected beer is {}. {}".format(name, description)
