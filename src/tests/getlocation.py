# -*- coding: utf-8 -*-

import re
import sys
import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
import json

ip = json.load(urlopen('http://httpbin.org/ip'))['origin']


geody = "http://www.geody.com/geoip.php?ip=" + str(ip)
html_page = urllib2.urlopen(geody).read()
soup = BeautifulSoup(html_page)

# Filter paragraph containing geolocation info.
paragraph = soup('p')[3]

# Remove html tags using regex.
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print geo_txt[32:].strip()