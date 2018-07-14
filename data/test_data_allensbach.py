# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import pandas as pd
from data.fetch_and_clean import get_table, cleaning_table
from data.urls_sonntagsfrage import SONNTAGSFRAGE_URL

#%% cleaning aktuell
table = get_table(SONNTAGSFRAGE_URL['allensbach']['aktuell'])
table_clean_aktuell = cleaning_table(table)

#%% cleaning 2013
table = get_table(SONNTAGSFRAGE_URL['allensbach']['2013'])
table.loc[10, 'Befragte'] = '1500'
table_clean_2013 = cleaning_table(table)

#%% cleaning 2009
table = get_table(SONNTAGSFRAGE_URL['allensbach']['2009'])
table_clean_2009 = cleaning_table(table)



#%%
table_full = pd.concat([table_clean_2017, table_clean_2013, table_clean_2009])

table_full['Institut'] = 'Allensbach'

#%%




