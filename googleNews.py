__author__ = 'Tyler Rudie'
import urllib
import urllib2

import simplejson


term = 'barack obama'

encoded = urllib.quote(term)
pages = ['0','4','8','12','16','20','24']
results = []
for i in pages:
        url = ('https://ajax.googleapis.com/ajax/services/search/news?' +
               'v=1.0&q='+
               encoded   +
               '&start=' +
               i)

        request = urllib2.Request(url, None, )
        response = urllib2.urlopen(request)

        # Process the JSON string.
        results = simplejson.load(response)
        for  a in results['responseData']['results']:
            print a['publishedDate'] + ' ' + a['publisher']

