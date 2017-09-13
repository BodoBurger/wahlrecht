# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import urllib3
import certifi 
import pandas as pd

from data.urls_sonntagsfrage import URL_ALLENSBACH

#%%
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


#%%
def get_table(url, table_number = 1):
    """
    """
    r = http.request('GET', url)
    table = pd.read_html(r.data)[table_number]
    
    return table

#%%
def cleaning_allensbach(table, columns_to_drop, rows_to_drop, columns_parties):
    """
    table: pandas DataFrame
    columns_to_drop: list with indices of empty columns
    rows_to_drop: list of rows that contain non-sensical entries
    columns_parties: list of indices of columns that contain parties
    """
    table = table.drop(table.columns[columns_to_drop], axis=1)
    table = table.drop(rows_to_drop, axis=0)
    table.columns.values[0] = 'Veröffentlichung'
    table['Veröffentlichung'] = pd.to_datetime(table['Veröffentlichung'], format='%d.%m.%Y')
    for col in table.columns.values[columns_parties]:
        table[col] = pd.to_numeric(table[col].str.replace('%', '').str.replace(',', '.').str.replace('–', ''))
    table['Befragte'] = pd.to_numeric(table['Befragte'].str.replace('≈', '').str.replace('?', '').str.replace('.', ''))
    
    return table
    

#%% cleaning 2017
table_clean_2017 = cleaning_allensbach(get_table(URL_ALLENSBACH['2017']), 
                                       [1,9,12,13], [48, 49], slice(1,8))

#%% cleaning 2013
table = get_table(URL_ALLENSBACH['2013'])
table.loc[10, 'Befragte'] = '1500'
table_clean_2013 = cleaning_allensbach(table, [1,10,13], [0, 52, 53], slice(1, 9))
del(table)

#%% cleaning 2009
table_clean_2009 = cleaning_allensbach(get_table(URL_ALLENSBACH['2009']), 
                                       [1,8,11], [0,52,53], slice(1,7))



#%%
table_full = pd.concat([table_clean_2017, table_clean_2013, table_clean_2009], ignore_index=True)

table_full['Institut'] = 'Allensbach'

#%%




