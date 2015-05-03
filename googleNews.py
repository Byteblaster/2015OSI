__author__ = 'Tyler Rudie'
import urllib
import urllib2

import simplejson
import xlsxwriter

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
print len(search)

workbook = xlsxwriter.Workbook('Expenses01.xlsx')
worksheet = workbook.add_worksheet('Data')
row = 0
for a in search:

    col = 0
    worksheet.write(row, col,     a.Term)
    worksheet.write(row, col + 1, a.Date)
    worksheet.write(row, col + 2, a.Publisher)
    worksheet.write(row, col + 3, a.Title)
    worksheet.write(row, col + 4, a.URL)

    row += 1

workbook.close()