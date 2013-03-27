To get this up and running (non-Windows):

> git clone https://github.com/cameronmaske/intoxicoders-beer-api.git intoxicoders

> virtualenv intoxicoders

> cd intoxicoders

> source bin/activate

> pip install -r requirements.txt


To run the two example Python scripts and see their output:

> python test.py
{u'currentPage': 1,
 u'data': [{u'abv': u'5',
            u'available': {u'description': u'Available year round as a staple beer.',
                           u'id': u'1',
                           u'name': u'Year Round'},
            u'availableId': 1,
            u'createDate': u'2012-01-03 02:43:22',
            u'glass': {u'createDate': u'2012-01-03 02:41:33',
                       u'id': 5,
                       u'name': u'Pint'},
            u'glasswareId': 5,
            u'id': u'eGtqKZ',
            u'isOrganic': u'N',
            u'labels': {u'icon': u'https://s3.amazonaws.com/brewerydbapi/beer/eGtqKZ/upload_rRWjE3-icon.png',
                        u'large': u'https://s3.amazonaws.com/brewerydbapi/beer/eGtqKZ/upload_rRWjE3-large.png',
                        u'medium': u'https://s3.amazonaws.com/brewerydbapi/beer/eGtqKZ/upload_rRWjE3-medium.png'},
            u'name': u'Heineken',
            u'status': u'verified',
            u'statusDisplay': u'Verified',
            u'style': {u'abvMax': u'5',
                       u'abvMin': u'4.3',
                       u'category': {u'createDate': u'2012-03-21 20:06:46',
                                     u'id': 8,
                                     u'name': u'North American Lager'},
                       u'categoryId': 8,
                       u'createDate': u'2012-03-21 20:06:46',
                       u'description': u'This style has low malt (and adjunct) sweetness, is medium bodied, and should contain no or a low percentage (less than 25%) of adjuncts. Color may be light straw to golden. Alcohol content and bitterness may also be greater. Hop aroma and flavor is low or negligible. Light fruity esters are acceptable. Chill haze and diacetyl should be absent. Note: Some beers marketed as "premium" (based on price) may not fit this definition.',
                       u'fgMax': u'1.014',
                       u'fgMin': u'1.01',
                       u'ibuMax': u'15',
                       u'ibuMin': u'6',
                       u'id': 97,
                       u'name': u'American-Style Premium Lager',
                       u'ogMin': u'1.044',
                       u'srmMax': u'6',
                       u'srmMin': u'2'},
            u'styleId': 97,
            u'updateDate': u'2012-11-23 14:53:58'}],
 u'numberOfPages': 1,
 u'status': u'success',
 u'totalResults': 1}


> python beer_me.py
What beer do you want to search for? ale
Your randomly selected beer is Hoptoberfest. Our hoppy take on a classic seasonal German style lager. Brewed with pale ale, caramel, and toasted Munich malts that attribute a sweet earthy malty flavor, toasted aroma, and a bright orange hue. German Tettnanger hops add an herbal peppery flavor and nose. 

One of my favorite parts about brewing this beer is that we’re participating in a seasonal brewing tradition that spans the globe. Since nearly all craft breweries take part in the Oktoberfest season, I like to try the different renditions side by side.

We use a traditional lager fermentation along side the traditional toasted Munich style malts. There are a lot of bready characters that come up during the brew. We wanted to brew a hoppier version of the brew, so we added Perle, Tettnang and Columbus hops.

The simple recipe hasn’t changed since we started brewing it in 2006.
