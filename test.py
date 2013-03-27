'''
Access the BreweryDB API to search for beers and return a JSON result.
API documentation available here: http://www.brewerydb.com/developers/docs-endpoint/beer_index#1
'''

# Load functionality from the Requests module
import requests

# Load "pretty print" to display our response in an easy-to-read, indented block
from pprint import pprint


# The 'beers' endpoint of the API
url = 'http://api.brewerydb.com/v2/beers/'

# A dictionary of parameters as "key: value" pairs
params = {
    'key': '6208ddfdc0ffb605cc28baee87e4dcd4',
    'name': 'heineken',
}

# Get the API's response from a GET request to the following URL:
# http://api.brewerydb.com/v2/beers/?key=6208ddfdc0ffb605cc28baee87e4dcd4&name=heineken
response = requests.get(url, params=params)

# Dislay the JSON data returned by the response
pprint(response.json())
