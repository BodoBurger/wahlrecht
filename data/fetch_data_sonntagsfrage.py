# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import pandas as pd
from data.fetch_and_clean import get_table, cleaning_table
from data.urls_sonntagsfrage import SONNTAGSFRAGE_URL

tables_full = []

#%% fetch allensbach
inst = 'allensbach'
tables = []

for year in SONNTAGSFRAGE_URL[inst].keys():
    print(year)
    table = get_table(SONNTAGSFRAGE_URL[inst][year])
    tables.append(cleaning_table(table))


table_full = pd.concat(tables, ignore_index=True, sort=False)
table_full['Institut'] = inst

tables_full.append(table_full)

#%% fetch emnid
inst = 'emnid'
tables = []

for year in SONNTAGSFRAGE_URL[inst].keys():
    print(year)
    table = get_table(SONNTAGSFRAGE_URL[inst][year])
    tables.append(cleaning_table(table))

table_full = pd.concat(tables, ignore_index=True, sort=False)
table_full['Institut'] = inst

tables_full.append(table_full)

#%% fetch forsa
inst = 'forsa'
tables = []

for year in SONNTAGSFRAGE_URL[inst].keys():
    print(year)
    table = get_table(SONNTAGSFRAGE_URL[inst][year])
    tables.append(cleaning_table(table))

table_full = pd.concat(tables, ignore_index=True, sort=False)
table_full['Institut'] = inst

tables_full.append(table_full)


#%%
data_all = pd.concat(tables_full, sort=False)

data_all = data_all.set_index(['Veröffentlichung', 'Institut'])

#%%


