# -*- coding: utf-8 -*-
import links as l
import apesmit

class Sitemap:
    def __init__(self,url):
        self.url = url
        
    def return_links(self):
        func = l.Links(self.url)
        in_links = func.site_links()
        return in_links
        
    def create_sitemap(self):
        sm=apesmit.Sitemap()
        links = self.return_links()
        for link in links:
            sm.add(link)
        
        out=open('sitemaps/sitemap.xml', 'w+')
        sm.write(out)
        out.close()
    
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        sm = Sitemap(url)
        sm.create_sitemap()
        print "Sitemap elkészítve. Elmentve: sitemaps/sitemap.xml"
        
    else:
        print "Hiba az oldal betöltésénél!"