# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:43:27 2017

@author: Bodo
"""

#%%
import certifi
import urllib3

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

r = http.request('GET', wiki)
r.data


#%%
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.data)

print(soup.prettify())

#%% Looking at the data
soup.title
soup.title.string

all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))

#%% Extracting table content
all_tables = soup.find_all('table')

main_table = soup.find('table', class_='wikitable sortable plainrowheaders')	
main_table

rows = main_table.find_all('tr')

A=[];B=[];C=[];D=[];E=[];F=[];G=[]

for row in rows:
    cells = row.find_all('td')
    states = row.find_all('th')
    if len(cells) == 6:
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

# creating a data frame
import pandas as pd

df = pd.DataFrame(A, columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
df.head()

