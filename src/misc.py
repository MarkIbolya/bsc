# -*- coding: utf-8 -*-

def check_if_exists(url):
    import requests
    try:
        response = requests.get(url)
        if response.status_code < 400:
            return True
        return False
    except:
        return False  # ha lekérni sem sikerül az URL-t, akkor vagy nem létezik, vagy helytelen


def get_ip(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    import socket
    return socket.gethostbyname(url)


def get_location(url):
    import csv
    import struct
    import socket
    import netaddr
    
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    try:
        url = url.split('/')[0]  # csak a tényleges domain kell ("www." rész maradhat)
    except:
        pass
        
    ip = get_ip(url)
    
    with open("text-files/ip_loc_modified.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        long_ip = int(netaddr.IPAddress(ip))
        for row in readCSV:
            if int(long_ip) >= int(row[0]) and int(long_ip) <= int(row[1]):
                return row[2]
    

def response_time(url, tests=1):
    from timeit import Timer
    from urllib2 import urlopen
    
    def fetch():
        page = urlopen(url)
        return page.info()
    
    sum = 0
    
    for i in range(tests):
        timer = Timer(fetch)
        sum += timer.timeit(1)
        
    return float(sum / tests)
    
    
def usa_response_time(url):
    from timeit import Timer
    from urllib2 import urlopen
    
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    
    page = urlopen("http://markibolya.com/response.php?url=" + url)
    resp = float(page.read())
    return resp


def page_size(url):
    import urllib2
    
    def response_size(num, egyseg='B'):
        for unit in ['', 'K', 'M']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, egyseg)
            num /= 1024.0
    
    page = urllib2.urlopen(url)
    content = page.read()
    
    return response_size(len(content))


def html_elem_numbers(url):
    import mechanize
    from bs4 import BeautifulSoup
    
    br = mechanize.Browser()
    html = br.open(url).read()
    soup = BeautifulSoup(html)
    
    dict = {}
    dict['div'] = 0
    dict["p"] = 0
    dict["header"] = 0
    dict["span"] = 0
    dict["h1"] = 0
    dict["h2"] = 0
    dict["a"] = 0
    
    for tag in soup.findAll('div'):
        dict["div"] += 1
    for tag in soup.findAll('p'):
        dict["p"] += 1
    for tag in soup.findAll('header'):
        dict["header"] += 1
    for tag in soup.findAll('span'):
        dict["span"] += 1
    for tag in soup.findAll('h1'):
        dict["h1"] += 1
    for tag in soup.findAll('h2'):
        dict["h2"] += 1
    for tag in soup.findAll('a'):
        dict["a"] += 1
    
    return dict


def comparison(url):
    if response_time(url) > usa_response_time(url):
        return "Egyesült Államokból a betöltési idö " + str(response_time(url) - usa_response_time(url)) + " másodperccel gyorsabb."
    else:
        return "Jelenlegi pozíciónkról a betöltési idö  " + str(usa_response_time(url) - response_time(url)) + " másodperccel gyorsabb."


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        if check_if_exists(url):
            print "Az oldal IP címe: " + get_ip(url)
            print "A szerver helye: " + get_location(url)
            print "Az oldal mérete: " + page_size(url)
            print "A HTML elemek száma: ", html_elem_numbers(url)
            print "Pozíciónkról a szerver válaszideje: ", response_time(url)
            print "Amerikai szerverröl a válaszidö: ", usa_response_time(url)
            print "Különbség: ", comparison(url)
        
    else:
        print "Hiba az oldal betöltésénél!"
    
    
    
