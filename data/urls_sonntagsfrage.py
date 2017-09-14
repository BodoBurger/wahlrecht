#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:22:01 2017

@author: bodo
"""
BASE = 'http://www.wahlrecht.de/umfragen/'

SONNTAGSFRAGE = {
        'allensbach': ['2002', '2005', '2009', '2013', '2013o', '2013w', '2017'],
        'emnid': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', '2017'],
        'forsa': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', '2017'],
        'dimap': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', '2017'],
        'insa': ['2017'],
}

SONNTAGSFRAGE_URL = {
    inst: {
        year: 
            (BASE+inst+'/'+year+'.htm' if year != '2017' else BASE+inst+'.htm')
        for year in years
    }
    for inst, years in SONNTAGSFRAGE.items()
}
