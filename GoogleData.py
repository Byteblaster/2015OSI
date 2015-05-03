from xgoogle.search import GoogleSearch, SearchError
try:
        gs = GoogleSearch("quantum mechanics")
        gs.results_per_page = 100
        results = []
        while True:
            tmp = gs.get_results()
            if not tmp: # no more results were found
                break
        results.extend(tmp)
        # ... do something with all the results ...
except SearchError, e:
        print "Search failed: %s" % e


for r in results:
    print r.title.encode('utf8')