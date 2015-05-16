# -*- coding: utf-8 -*-
import urllib
import json

class shareCount:
    def __init__(self, url):
        self.url = url
    
    def facebook(self):
        try:
            response = urllib.urlopen("http://graph.facebook.com/?id=" + self.url);
            data = json.loads(response.read())
            try:
                return data['shares']
            except:
                return 0
        except:
            return 0
    
    def twitter(self):
        response = urllib.urlopen("http://urls.api.twitter.com/1/urls/count.json?url=" + self.url);
        data = json.loads(response.read())
        return data['count']
    
    def stumbleupon(self):
        try:
            response = urllib.urlopen("http://www.stumbleupon.com/services/1.01/badge.getinfo?url=" + self.url);
            data = json.loads(response.read())
            return int(data['result']['views'])
        except:
            return 0
        
    def linkedin(self):
        response = urllib.urlopen("http://www.linkedin.com/countserv/count/share?url=" + self.url + "&format=json");
        data = json.loads(response.read())
        return int(data['count'])
    
    def googleplus(self):
        try:
            from bs4 import BeautifulSoup
            response = urllib.urlopen("https://plusone.google.com/_/+1/fastbutton?url=" + self.url).read();
            html = BeautifulSoup(response)
            string = html.findAll('div', { "class" : "Oy" })[0].text #0y classban van a megosztások száma stringként ha 999 fölött van
            if string[-1]=="M":
                string = string.strip("M")
                num=int(float(string)*1000000)
            elif string[-1]=="k":
                string = string.strip("k")
                num=int(float(string)*1000)
            else:
                num=int(string)
            return num
        except:
            return 0
        
    def all_shares(self,googleplus=False):
        num = int(self.facebook())+int(self.twitter())+int(self.linkedin())
        if googleplus==True:
            num+=self.googleplus()
        return num
        
        
    
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    s = shareCount(url)
    from misc import check_if_exists
    if check_if_exists(url):
        print "Stumbleupon: ",s.stumbleupon()
        print "Facebook: ",s.facebook()
        print "Google+: ",s.googleplus()
        print "Twitter: ",s.twitter()
        print "LinkedIn: ",s.linkedin()
        print "Az összes megosztás száma: ",s.all_shares(True)
        
    
    
    else:
        print "Hiba az oldal betöltésénél!"
    
    
    
    
    
    
    
