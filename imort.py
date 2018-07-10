# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:56:09 2018

@author: Administrator
"""
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import os

trainFile = 'C:/Users/Administrator/Desktop/curtains/SalesDashboard-7-9-18.csv'
#pwd = os.getcwd()
#os.chdir(os.path.dirname(trainFile))
to_num = lambda x: float(x.replace('$','').replace(',',''))
sells = pd.read_csv(trainFile,nrows=9,skiprows=14,index_col=0,usecols=[0,1,2],\
                   converters={1:to_num})
#单个字符串可以操作，放入converters却不可以？？