# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from global_info import *

# oxford.com - structure
# <ol class="senses_multiple">
#     <li class="sense"> * n
#         <span class="def" htag="span" hclass="def">
#         <ul class="examples" htag="ul" hclass="examples">
#             <li class="" htag="li"> * n

def search(query):
    req = request.Request(
        url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{query}",
        headers = headers
    )

    html = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(html, 'html.parser')

    body = soup.find("ol", "senses_multiple")

    index = 1

    for li in body.find_all("li", "sense"):
        definition = li.find("span", "def").get_text()
        example = li.ul.li.get_text()
        print(f"{index}. {definition}\n")
        print(f"Eg. {example}")
        print("----------------------------")
        index += 1
