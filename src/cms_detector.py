# -*- coding: utf-8 -*-
class CmsDetector:
    def __init__(self, url):
        from bs4 import BeautifulSoup
        import mechanize
        import random
        self.url = url
        USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                   'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                   'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')
        
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders=[('User-agent',random.choice(USER_AGENTS))]
        
        html = br.open(self.url).read()
        self.soup = BeautifulSoup(html)
    
    def wordpress(self):
        for link in self.soup.findAll('link'):
            if "wp-content" in str(link):
                return True
        return False
    
    def joomla(self):
        for link in self.soup.findAll('script'):
            if "joomla" in str(link):
                return True
            for link in self.soup.findAll('link'):
                if "joomla" in str(link):
                    return True
        return False
    
    def jquery(self):
        for link in self.soup.findAll('script',{"src":True}):
                if "jquery" in str(link):
                    return True
        return False
    
    def drupal(self): # sokszor nem müködik
        for link in self.soup.findAll('script'):
            if "drupal" in str(link):
                return True
        return False

    def test(self):
        if self.jquery()==True:
            print "jQuery"
        if self.wordpress() == True:
            return "Wordpress"
        elif self.joomla() == True:
            return "Joomla"
        elif self.joomla() == True:
            return "Drupal"
        return "Nem található CMS"
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        detector = CmsDetector(url)
        print detector.test()
    else:
        print "Hiba az oldal betöltésénél!"
    