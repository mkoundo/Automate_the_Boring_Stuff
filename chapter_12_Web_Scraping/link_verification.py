#! python3
# link_verification.py
# Author: Michael Koundouros
"""
Write a program that, given the URL of a web page, will attempt to download every linked page on the page. The
program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://automatetheboringstuff.com/'

res = requests.get(url)                                     # download site html
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')               # convert html into a soup object

a_tags = soup.find_all('a')                                 # search soup for all <a> tags

print('Checking links...')
for tag in a_tags:
    link = tag.attrs.get('href', None)                      # extract url from each a tag
    if link is not None:
        if link[0] == '/':                                  # check if link is relative to site
            link = url + link[1:]
        res = requests.get(link)
        try:
            res.raise_for_status()
            print(f'Link OK: {link}')
        except Exception as exc:
            if res.status_code == 404:                      # Only raise 404 errors
                print(f'Broken Link: {exc}')
