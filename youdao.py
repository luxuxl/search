# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request

# youdao.com - structure
# EN
# <ul class="basic">
#     <li class="word-exp"> * n
#         <span class="pos">
#         <span class="trans">
# CN
# <ul class="basic">
#     <div class="col2"> * n
#         <div class="trans-ce">
#         <div class="word-exp_tran grey">

def search(query):
    req = request.Request(url = f"https://youdao.com/result?word={query}&lang=en")

    html = request.urlopen(req).read().decode('utf8')
    
    soup = BeautifulSoup(html, 'html.parser')
    
    body = soup.find("ul", "basic")

    # handle english query
    for li in body.find_all("li", "word-exp"):
        mean = li.get_text()
        mean = mean.split("；",3)
        if len(mean) == 4:
            mean.pop()
        print('; '.join(mean))
        print("--------------------------------------")

    # handle chinese query
    for div in body.find_all("div", "col2"):
        title = div.find("div", "trans-ce")
        print(title.get_text(), '\n')
        content = div.find("div", "word-exp_tran grey").get_text()
        content = content.split("；",3)
        if len(content) == 4:
            content.pop()
        print('; '.join(content))
        print("--------------------------------------------------")