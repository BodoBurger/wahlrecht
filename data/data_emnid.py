# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import pandas as pd
from data.fetch_and_clean import get_table, cleaning_table
from data.urls_sonntagsfrage import URL_EMNID

#%% cleaning 2017
table = get_table(URL_EMNID['2017'])
table_clean_2017 = cleaning_table(table)

#%% cleaning 2013
table = get_table(URL_EMNID['2013'])
table_clean_2013 = cleaning_table(table)

#%% cleaning 2008
table = get_table(URL_EMNID['2008'])
table_clean_2008 = cleaning_table(table)

#%%
table_full = pd.concat([table_clean_2017, table_clean_2013, table_clean_2008])

table_full['Institut'] = 'Emnid'
