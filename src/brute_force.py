# -*- coding: utf-8 -*-

import mechanize
import random

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')


url = "http://evsum.com/bcmunka/"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent',random.choice(USER_AGENTS))]

response = br.open(url)

for form in br.forms():
    print "Form name:", form.name
    print form

br.form = list(br.forms())[0]

br.form['account'] = 'admin'
br.form['password'] = 'pass'

br.method = "POST"
response = br.submit()
print response.geturl() #url to which the page has redirected after login