def response_time(url):
    from timeit import Timer
    from urllib2 import urlopen
    
    def fetch():
        page = urlopen(url)
        return page.info()
    
    sum = 0
    
    for i in range(3):
        timer = Timer(fetch)
        sum += timer.timeit(1)
        
    return sum / 3
    
if __name__ == '__main__':
    print response_time('http://google.com')
