# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import certifi
import urllib3

url = 'http://www.wahlrecht.de/umfragen/allensbach.htm'

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

r = http.request('GET', url)
r.data

#%%
from bs4 import BeautifulSoup

data = BeautifulSoup(r.data, "lxml")

print(data.prettify())

#%%
#%% Extracting table content
main_table = data.find('table', class_='wilko')	
main_table

rows = main_table.find_all('tr')
rows[0]
rows[1]
rows[2]
rows[3]
