__author__ = 'Tyler Rudie'


class article(object):
        Date      = ''
        Publisher = ''
        Title     = ''
        URL       = ''

        def __init__(self, Date, Publisher, Title, URL):
            self.Date       = Date
            self.Publisher  = Publisher
            self.Title      = Title
            self.URL        = URL

def new_article ( Date, Publisher, Title, URL):
    return article(Date, Publisher, Title, URL)