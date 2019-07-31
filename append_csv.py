# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:54:16 2019

@author: anthony.macko
"""

import pandas as pd
import glob

def appendcsvs(path):
    allFiles = glob.glob(path + "/*.csv")

    list_ = []

    for file_ in allFiles:
        
        df = pd.read_csv(file_,index_col=None, header=0 ,encoding = 'ISO-8859-1',error_bad_lines=False,low_memory = False)
        list_.append(df)

    df = pd.concat(list_, axis = 0, ignore_index = True )

    return df