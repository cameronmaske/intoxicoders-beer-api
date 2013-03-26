import requests

#http://www.brewerydb.com/developers/docs-endpoint/search_index
url = 'http://api.brewerydb.com/v2/search'

query = raw_input('What beer do you want to search for?: ')
params = {
    'key': '6208ddfdc0ffb605cc28baee87e4dcd4',
    'q': query,
    'type': 'beer'
}

response = requests.get(url, params=params)
json = response.json()

from random import choice
beers = json['data']
randomly = choice(beers)

name = randomly['name']

try:
    description = randomly['description'].encode('utf-8')
except:
    description = 'No description available.'

print "Your randomly selected beer is {}. {}".format(
    name, description
    )