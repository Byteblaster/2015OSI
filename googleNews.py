__author__ = 'Tyler Rudie'
import urllib
import urllib2

import simplejson

import DataObject


def searchGoogleNews(Term):
    encoded = urllib.quote(Term)
    pages = ['0', '4', '8', '12', '16', '20', '24', '28', '32', '36', '40', '44', '48', '52', '56', '60']
    data = []
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
            if results['responseStatus'] == 200:
                for record in results['responseData']['results']:

                    data.append(DataObject.new_article(record['publishedDate'],
                                                       record['publisher'],
                                                       record['title'],
                                                       record['url'],
                                                       Term))

    return data



term = 'barack obama'

search = searchGoogleNews(term)
for a in search:

    print a.Date

print len(search)