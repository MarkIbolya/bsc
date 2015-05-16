# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib

def validator(url):
    response = urllib.urlopen("https://validator.w3.org/check?uri="+url+"&charset=%28detect+automatically%29&doctype=Inline&group=0").read();
    html = BeautifulSoup(response)
    try:
        result = html.findAll('h2', { "id" : "results" })[0].text
        errors = html.findAll('td', { "class" : "invalid" })[0].text
        valid = False
    except:
        valid = True
    
    if valid == False:
        return "Hibás HTML kód! Hibaüzenet: " + str(result).strip() +" "+ str(errors).strip()
    else:
        return "Az oldal megfelel a HTML szabályainak!"
    
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        print validator(url)
    
    else:
        print "Hiba az oldal betöltésénél!"