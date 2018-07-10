# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

fpath = 'C:/Users/Administrator/Downloads/新建文件夹/库存盘点 20180625 NEWLAKE.csv'
with open(fpath,'r') as newlake:
    doc = newlake.read()
    pat = re.compile(',+')
    trunc_doc = pat.sub('\t',doc)
    
wpath = 'C:/Users/Administrator/Downloads/新建文件夹/newlake.txt'
with open(wpath,'w',encoding='utf-8') as trunc:
    trunc.write(trunc_doc)

    