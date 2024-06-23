# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import curses
from urllib import request

query = "beauty"

query = request.pathname2url(query)

headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)",
    "Accept": "text/html",
    "Cookie": ""
}

url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{query}"

req = request.Request(url,headers=headers)


req = request.Request(url=url,headers=headers)

result = request.urlopen(url).read().decode('utf8')

text = BeautifulSoup(result, 'html.parser').find_all(attrs={"class": "b_algo"})


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    links = []
    for a in soup.find_all('a', href=True):
        links.append((a.get_text(), a['href']))
    return text, links

def render_text(stdscr, text):
    stdscr.clear()
    stdscr.addstr(0, 0, text)
    stdscr.refresh()

def main(stdscr):
    curses.echo()
    stdscr.addstr(0, 0, "Enter URL: ")
    url = stdscr.getstr().decode('utf-8')
    html = fetch_page(url)
    if html:
        text, links = parse_html(html)
        render_text(stdscr, text)
        while True:
            stdscr.addstr(curses.LINES - 1, 0, "Press 'q' to quit, 'n' to enter new URL")
            key = stdscr.getch()
            if key == ord('q'):
                break
            elif key == ord('n'):
                stdscr.clear()
                stdscr.addstr(0, 0, "Enter URL: ")
                url = stdscr.getstr().decode('utf-8')
                html = fetch_page(url)
                if html:
                    text, links = parse_html(html)
                    render_text(stdscr, text)

if __name__ == '__main__':
    curses.wrapper(main)
