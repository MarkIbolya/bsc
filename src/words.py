# -*- coding: utf-8 -*-

def words_freq(url):
    import urllib
    import random
    import mechanize
    from bs4 import BeautifulSoup
    USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5')
    
    common = open("text-files/common_words_en.txt").read().split("\n")
        
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders=[('User-agent',random.choice(USER_AGENTS))]
    
    html = br.open(url).read()
    soup = BeautifulSoup(html)

    [s.extract() for s in soup('script')]  # ignoráljuk a javascriptet

    word_dict = {}
    word_list = []
    
    i = 0
    
    for link in soup.findAll(text=True):
        try:
            word_list += link.lower().split()
        except:
            pass
    
    for w in word_list:
        if w.encode('utf-8') not in common and w.isalpha():
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1
    
    top_words = sorted(word_dict.items(), key=lambda(k, v):(v, k), reverse=True)[:100]
    
    for words in top_words:
        yield words

if __name__ == '__main__':
    import sys          
    url = raw_input('Url: ').split()
    for i in words_freq(url[0]):
        print i[0].encode('utf-8')+str(i[1])
