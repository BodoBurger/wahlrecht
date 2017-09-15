#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:22:01 2017

@author: bodo
"""

BASE = 'http://www.wahlrecht.de/umfragen/'

SONNTAGSFRAGE = {
        'allensbach': ['2002', '2005', '2009', '2013', 'aktuell'], #'2013o', '2013w', 
        'emnid': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', 'aktuell'],
        'forsa': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', 'aktuell'],
        'dimap': ['1998', '1999', '2001', '2002', '2003', '2004', '2005', '2006',
                  '2007', '2008', '2013', 'aktuell'],
        'insa': ['aktuell'],
}

SONNTAGSFRAGE_GRUPPE_WAHLEN = ['1998', '2002', '2005', '2009', '2013', 'aktuell']

SONNTAGSFRAGE_URL = {
    inst: {
        year: 
            (BASE+inst+'/'+year+'.htm' if year != 'aktuell' else BASE+inst+'.htm')
        for year in years
    }
    for inst, years in SONNTAGSFRAGE.items()
}

SONNTAGSFRAGE_URL['gruppe_wahlen_projektion'] = {
    year: 
        (BASE+'politbarometer/politbarometer-'+year+'.htm' if year != 'aktuell' else BASE+'politbarometer.htm')
    for year in SONNTAGSFRAGE_GRUPPE_WAHLEN
}

SONNTAGSFRAGE_URL['gms_projektion'] = {
        'aktuell': 'http://www.wahlrecht.de/umfragen/gms.htm',
        '2009': 'http://www.wahlrecht.de/umfragen/gms/projektion-2009.htm',
        '2005': 'http://www.wahlrecht.de/umfragen/gms/projektion-2005.htm',
}

    