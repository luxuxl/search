# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from global_info import *

# google.com - structure
# <div>
#     <div class="ezO2md">
#         <a class="fuLhoc ZWRArf">
#             <span class="CVA68e qXLe6d fuLhoc ZWRArf">
#             <span class="qXLe6d dXDvrc">
#         <span class="qXLe6d FrIlee">
#             <span class="fYyStc">

def search(query):
    req = request.Request(
        url = f"https://www.google.com/search?q={query}",
        headers = headers
    )

    html = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(html, 'html.parser')

    body = soup.find_all("div", "ezO2md")

    for each in body:
        try:
            a = each.find("a", "fuLhoc ZWRArf")
            title = a.find("span", "CVA68e qXLe6d fuLhoc ZWRArf").get_text()
            link = a.find("span", "qXLe6d dXDvrc").get_text()
            description = each.find("span", "qXLe6d FrIlee").find("span", "fYyStc").get_text()
        except:
            continue

        print(title + f" - ({link})")
        print("\n")
        print(description)
        print("--------------------------------------------------")
