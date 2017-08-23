# ! python3.
# !/usr/bin/env python
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4

print('Googling...')    #displays ths while downloading the page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# this retieves top search result search result links

# opens a browser for each result

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# open a browser tab for each result
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
