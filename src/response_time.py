def response_time(url):
    from timeit import Timer
    from urllib2 import urlopen
    
    def fetch():
        page = urlopen(url)
        return page.info()
    
    timer = Timer(fetch)
    print timer.timeit(1)