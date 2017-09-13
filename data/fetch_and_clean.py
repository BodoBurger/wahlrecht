# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 22:37:28 2017

@author: Bodo
"""
#%%
import urllib3
import certifi 
import pandas as pd

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
def cleaning_table(table, columns_to_drop = None, rows_to_drop = None, party_columns = None):
    """
    table: pandas DataFrame
    
    columns_to_drop: list with indices of empty columns
    rows_to_drop: list of rows that contain non-sensical entries
    party_columns: list of indices of columns that contain parties
    """
    # cleaning rows
    table = table.query('Befragte != "Bundestagswahl" and Befragte != "Befragte"')
    if rows_to_drop:
        table = table.drop(rows_to_drop, axis=0)

    # cleaning columns
    table = table.dropna(axis=1, how='all')
    if columns_to_drop:
        table = table.drop(table.columns[columns_to_drop], axis=1)
    
    table.index = pd.to_datetime(table.iloc[:, 0], format='%d.%m.%Y')
    table = table.drop('Unnamed: 0', axis=1)
    
    # clean party columns
    if party_columns:
        columns = table.columns.values[party_columns]
    else:
        columns = []
        for col in table.columns.values:
            if col not in ['Befragte', 'Zeitraum']:
                columns.append(col)
    for col in columns:
        table[col] = pd.to_numeric(table[col].str.replace('%', '').str.replace(',', '.').str.replace('–', ''))
    
    table['Befragte'] = pd.to_numeric(table['Befragte'].str.replace('≈', '').str.replace('?', '').str.replace('.', ''))
    
    return table
