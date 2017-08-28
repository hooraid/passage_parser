import requests
import sys
import re
import json
from bs4 import BeautifulSoup


#url = str(sys.argv[1]);

with open('download.txt') as f:
    urls = f.readlines()
url_list = urls


a=0
for url in url_list:
    url = url.rstrip('\n')
    print(url)
    req = requests.get(url);
    html = req.text;

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('h1', attrs={'id':'firstHeading'})
    text=soup.find_all('div', attrs={'class':'mw-parser-output'})
    text = text[0].find_all('p')


    idx = 0
    print(title[0].text);
    for para in text:
        if para.find('img'):
            continue
        if para.find('video'):
            continue
        tt = re.sub(r'\[[^]]*\]', '', re.sub(r'\([^)]*\)', '',para.text))
        tt = re.sub(r'\{[^}]*\}', '', tt);
        if len(tt)<200:
            continue
        jsontext = {
            'sPTITLE' : title[0].text,
            'nPNUM' : idx,
            'sCONTENT' : tt,
            'sURL' : url
        }
        idx=idx+1
    print(idx)
    a = a+idx;
print(a)
