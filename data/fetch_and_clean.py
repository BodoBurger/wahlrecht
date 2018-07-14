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
def get_table(url, table_number=1):
    """
    """
    request_table = http.request('GET', url)
    #table = pd.read_html(r.data, parse_dates=True, decimal=',', thousands = '.')[table_number]
    # Does not parse dates in correct form
    table = pd.read_html(request_table.data)[table_number]

    return table

#%%
def cleaning_table(table, columns_to_drop=None, rows_to_drop=None, party_columns=None):
    """
    table: pandas DataFrame

    columns_to_drop: list with indices of empty columns to drop manually
    rows_to_drop: list of rows that contain non-sensical entries to drop manually
    party_columns: list of indices of columns that contain parties. Use case?
    """

    table = table.rename(columns={'\xa0': 'Veröffentlichung', 'Unnamed: 0': 'Veröffentlichung'})
    table['Veröffentlichung'] = pd.to_datetime(table['Veröffentlichung'], format='%d.%m.%Y',
                                               errors='coerce')

    # cleaning rows
    table = table.dropna(subset=['Veröffentlichung'])
    if 'Befragte' in table.columns:
        table = table.query('Befragte != "Bundestagswahl"')
    if rows_to_drop:
        table = table.drop(rows_to_drop, axis=0)

    # cleaning columns
    table = table.dropna(axis=1, how='all')
    if columns_to_drop:
        table = table.drop(table.columns[columns_to_drop], axis=1)

    # clean party columns
    if party_columns:
        columns = table.columns.values[party_columns]
    else:
        columns = []
        for col in table.columns.values:
            if col not in ['Veröffentlichung', 'Befragte', 'Zeitraum']:
                columns.append(col)
    for col in columns:
        table[col] = table[col].str.replace('%|–', '').str.replace(',', '.')
        try:
            table[col] = pd.to_numeric(table[col])
        except ValueError:
            table[col] = handle_value_errors(table[col].copy())

            table[col] = pd.to_numeric(table[col]) # try conversion again

    # clean 'Befragte'
    if 'Befragte' in table.columns:
        if table['Befragte'].dtype == 'object':
            table['Befragte'] = pd.to_numeric(
                table['Befragte'].str.replace(r'≈|~|\?|\.|>', '')
            )
        elif table['Befragte'].dtype == 'float64':
            # this is only a hack because you cannot specify dtype in read_html
            table['Befragte'] = table['Befragte'].apply(lambda x: 1000*x if x < 10 else x)
    return table

def handle_value_errors(table_col):
    """Handle exceptional entries
    """
    # catch '30-32%':
    ind = table_col.str.match(r'\d\d?-\d\d?')
    if sum(ind) > 0:
        res_new = []
        for res in table_col[ind].values:
            tmp = res.strip().split('-')
            res_new.append(str((float(tmp[1])+float(tmp[0]))/2))
        table_col.loc[ind] = res_new
    # catch explicit 'not specified' like 'k. A.':
    ind2 = table_col.str.match('k. A.')
    if sum(ind2) > 0:
        table_col.loc[ind2] = ''
    # catch Piraten mixed with Sonstige:
    # e.g. 'PIR 3 %Sonst. 5 %' in column 'Sonstige
    ind3 = table_col.str.match(r'PIR \d')
    if sum(ind3) > 0:
        table_col.loc[ind3] = ''

    return table_col
