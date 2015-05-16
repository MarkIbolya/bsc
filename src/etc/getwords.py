import urllib
from bs4 import BeautifulSoup

url = "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Hungarian_frequency_list_1-10000"

text = open("words.txt", "w+")

htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)

i = 0
for div in soup.select('div[id=mw-content-text]'):
    for szo in div.findAll('a'):
        i += 1
        text.write((szo.text+"\n").encode('utf-8'))
        if i==151:
            break