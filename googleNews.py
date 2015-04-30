__author__ = 'Tyler Rudie'
import urllib2

import simplejson


url = ('https://ajax.googleapis.com/ajax/services/search/news?' +
       'v=1.0&q=barack%20obama&start=16' )

request = urllib2.Request(url, None, )
response = urllib2.urlopen(request)

# Process the JSON string.
results = simplejson.load(response)
# now have some fun with the results...
print results['responseData']['cursor']['pages']

for  a in results['responseData']['results']:
    print a['publishedDate'] + ' ' + a['publisher']

