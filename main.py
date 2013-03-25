import requests
from random import choice
from pprint import pprint

url = 'http://api.brewerydb.com/v2/beers/'
params = {
    'key': '6208ddfdc0ffb605cc28baee87e4dcd4',
}

if __name__ == "__main__":
    params['name'] = raw_input('What beer do you want to look up?: ')

    response = requests.get(url, params=params)
    beers = response.json().get('data')

    if beers:
        print "Found {} beer(s)!".format(len(beers))
    else:
        print "Found no beers :("

    randomly = choice(beers)

    style = randomly.get('style')
    if style:
        category = style.get('category')
        description = style.get('description')
    else:
        category = 'No category'
        description = 'No description'

    print "Your randomly selected beer is {} [{}]- {}".format(
        randomly['name'],
        category,
        description)


    url = 'http://api.brewerydb.com/v2/beer/{}/ingredients'.format(randomly['id'])
    params = {
        'key': '6208ddfdc0ffb605cc28baee87e4dcd4',
    }

    response = requests.get(url, params=params).json()
    pprint(response)


    ingredients = response.get('data', 'No ingredients available')

    pprint(ingredients)
