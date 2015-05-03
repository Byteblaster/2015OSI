__author__ = 'Tyler Rudie'


class article(object):
        Date      = ''
        Publisher = ''
        Title     = ''
        URL       = ''
        Term      = ''

        def __init__(self, Date, Publisher, Title, URL, Term):
            self.Date       = Date
            self.Publisher  = Publisher
            self.Title      = Title
            self.URL        = URL
            self.Term       = Term
            
            
def new_article(Date, Publisher, Title, URL, Term):

    return article(Date, Publisher, Title, URL, Term)