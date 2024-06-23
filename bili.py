# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib import request
from global_info import *

# bilibili.com - structure
# <ul class="video-list clearfix">
#     <div class="info"> * n
#         <a class="title" href="//www.bilibili.com/video/?seid=13107056418744793102">
#         <span class="tag-item uper">
# ------- or -------
# <div class="video i_wrapper search-all-list">
#     <div class="video-list row">
#         <div class="bili-video-card"> * n
#             <div class="bili-video-card__info--right">
#                 <a href="//www.bilibili.com/video/BV1Af421X7Kg/"> title
#                 <p class="bili-video-card__info--bottom"> author


def search(query):
    req = request.Request(
        url = f"https://search.bilibili.com/all?keyword={query}",
        headers = headers
    )

    html = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(html, 'html.parser')

    body = soup.find("ul", "video-list clearfix")

    for div in body.find_all("div", "info"):
        a = div.find("a", "title")
        title = a.get_text()
        link = a["href"]
        uper = div.find("span", "tag-item uper").get_text()
        if uper in title:
            print(title)
        else:
            print(f"{title} - ({uper})")
        print("-----------------------------")

