# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from global_info import *
# bing.com - parameters
# https://learn.microsoft.com/zh-cn/bing/search-apis/bing-web-search/reference/query-parameters

# bing.com - structure
# <ol id="b_results" class="">
#     <li class="b_algo" data-id=""> * n
#         <h2 style=""><a>
#         <div class="b_caption">

def search(query):
    req = request.Request(
        url = f"https://cn.bing.com/search?q={query}&PC=U316&FORM=CHROMN&first={start}&count={count}",
        headers = headers
    )

    html = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(html, 'html.parser')

    body = soup.find(id="b_results")

    for li in body.find_all("li", "b_algo"):
        h2 = li.find("h2").find("a")
        title = h2.get_text()
        link = h2.get("href")
        description = li.find("div", "b_caption").get_text()
        print(title + f" - ({link})")
        print("\n")
        print(description)
        print("--------------------------------------------------")

