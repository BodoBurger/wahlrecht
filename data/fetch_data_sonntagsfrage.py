# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import pandas as pd
from data.fetch_and_clean import get_table, cleaning_table
from data.urls_sonntagsfrage import SONNTAGSFRAGE_URL

#%%
tables_full = []

#%% fetch allensbach
inst = 'allensbach'
tables = []

for year in SONNTAGSFRAGE_URL[inst].keys():
    print(year)
    table = get_table(SONNTAGSFRAGE_URL[inst][year])
    tables.append(cleaning_table(table))


table_full = pd.concat(tables, ignore_index=True)
table_full['Institut'] = inst

tables_full.append(table_full)

#%% fetch emnid
inst = 'emnid'
tables = []

for year in SONNTAGSFRAGE_URL[inst].keys():
    print(year)
    table = get_table(SONNTAGSFRAGE_URL[inst][year])
    tables.append(cleaning_table(table))

table_full = pd.concat(tables, ignore_index=True)
table_full['Institut'] = inst

tables_full.append(table_full)

#%%
data_all = pd.concat(tables_full)

data_all = data_all.set_index(['Veröffentlichung', 'Institut'])

##%%
#table = get_table(SONNTAGSFRAGE_URL['emnid']['1998'])
#table_clean_1998 = cleaning_table(table)
#
##%%
#table = get_table(SONNTAGSFRAGE_URL['emnid']['2003'])
#table_clean_2003 = cleaning_table(table)
#
##%% cleaning 2013
#table = get_table(SONNTAGSFRAGE_URL['emnid']['2013'])
#table_clean_2013 = cleaning_table(table)
#
##%% cleaning 2008
#table = get_table(SONNTAGSFRAGE_URL['emnid']['2008'])
#table_clean_2008 = cleaning_table(table)
