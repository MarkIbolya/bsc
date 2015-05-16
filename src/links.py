# -*- coding: utf-8 -*-

import urlparse
import urllib
from bs4 import BeautifulSoup
import mechanize
import random

class Links:
    def __init__(self, url):
        self.url = url
        self.USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                       'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                       'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                       'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')
        
    def site_links(self):
        urls = [self.url]  # az összes url
        visited = [self.url]  # a már látogatott urlek
        
        while len(urls) > 0:
            if ".zip" in urls[0] or ".doc" in urls[0] or ".rar" in urls[0] or ".ppt" in urls[0]: # nem vesszük figyelembe a fájlokat
                    urls.pop(0)
                    continue
            try:
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.addheaders=[('User-agent',random.choice(self.USER_AGENTS))]
                
                htmltext = br.open(urls[0]).read()
            except:
                print urls[0]  # ha az url nem megnyitható
                continue
            soup = BeautifulSoup(htmltext)
            urls.pop(0)
            # print len(urls) # ennyi darab url-t találtunk meg eddig
            for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(self.url, tag['href'])
                if self.url in tag['href'] and tag['href'] not in visited:
                    urls.append(tag['href'])
                    visited.append(tag['href'])
                    #print urls[-1] # kiíratrjuk az utolsó megtalált url-t a jelenlegi oldalon
                    
        return visited  # visszatérési érték az összes megtalált url
    
    def out_links(self):
        from tld import get_tld
        
        urls = [self.url]  # az összes url
        visited = [self.url]  # a már látogatott urlek
        out = []
        
        
        domain = get_tld(self.url)
        
        while len(urls) > 0:
            try:
                if ".zip" in urls[0] or ".doc" in urls[0] or ".rar" in urls[0] or ".ppt" in urls[0]:
                    urls.pop(0)
                    continue
                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.addheaders=[('User-agent',random.choice(self.USER_AGENTS))]
                
                html = br.open(urls[0]).read()
                
            except:
                print "Nem nyitható meg: ", visited[0]  # ha az url nem megnyitható
                
                continue
            
            soup = BeautifulSoup(html)
            urls.pop(0)
            # print len(urls) # ennyi darab url-t találtunk meg eddig
            
            for tag in soup.findAll('a', href=True):
                tag['href'] = urlparse.urljoin(self.url, tag['href'])
                
                if domain not in tag['href'] and tag['href'] not in out:
                    out.append(tag['href'])
                    #print tag['href'] # megtalált URL
                    
                if self.url in tag['href'] and tag['href'] not in visited:
                    urls.append(tag['href'])
                    visited.append(tag['href'])
                #print tag['href']
        return out  # visszatérési érték az összes megtalált url
    
    
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        if len(sys.argv)>2:
            if sys.argv[2]=="be":
                links = Links(url)
                for link in links.site_links():
                    print link
            else:
                links = Links(url)
                for link in links.out_links():
                    print link
        else:
            links = Links(url)
            for link in links.out_links():
                print link
    else:
        print "Hiba az oldal betöltésénél!"    
    
    
    
    
    
    
    
    
    
    
