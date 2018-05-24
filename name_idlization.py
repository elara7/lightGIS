# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:21:27 2018

@author: elara
"""

import os
import pandas as pd
Province_path = 'D:\light_guo\Light_Guo\polygon\Province_polygon'
City_path = 'D:\light_guo\Light_Guo\polygon\City_Polygon'
Province_rename_path = 'D:\light_guo\Light_Guo\polygon\Province_rename'
City_rename_path = 'D:\light_guo\Light_Guo\polygon\City_rename'


# 建立名称索引
def name_list(path):
    name_list = list(set([i.split('.')[0] for i in os.listdir(path)]))
    _id=0
    for i in range(len(name_list)):
        name_list[i] = [name_list[i],_id]
        _id += 1
    return pd.DataFrame(name_list)

Province_id = name_list(Province_path)
City_id = name_list(City_path)

Province_id.to_csv('D:/light_guo/Light_Guo/name_id/'+'Province_id.csv',header=None,index=None,encoding='gbk')
City_id.to_csv('D:/light_guo/Light_Guo/name_id/'+'City_id.csv',header=None,index=None,encoding='gbk')

Province_dict={}
for i in range(len(Province_id)):
    Province_dict[Province_id.iloc[i,0]]=Province_id.iloc[i,1]
City_dict={}
for i in range(len(City_id)):
    City_dict[City_id.iloc[i,0]]=City_id.iloc[i,1]
    


for i in os.listdir(Province_path):
    name = i.split('.')[0]
    name_id = Province_dict[name]
    file_path = os.path.join(Province_path,i)
    rename_path = os.path.join(Province_rename_path,str(name_id)+'.'+i.split('.',1)[1])
    os.rename(file_path,rename_path)


for i in os.listdir(City_path):
    name = i.split('.')[0]
    name_id = City_dict[name]
    file_path = os.path.join(City_path,i)
    rename_path = os.path.join(City_rename_path,str(name_id)+'.'+i.split('.',1)[1])
    os.rename(file_path,rename_path)