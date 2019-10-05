#河南机电职业学院 信息工程学院
#2017级 大数据技术与应用-17-1 王壮

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class data_clean(object):
    def __init__(self):
        pass

    def get_data(self):  #读取数据
        data1 = pd.read_csv('F:\\Data cleaning\\data_analysis.csv', encoding='gbk')
        data2 = pd.read_csv('F:\\Data cleaning\machine_learning.csv', encoding='gbk')
        data3 = pd.read_csv('F:\\Data cleaning\data_mining.csv', encoding='gbk')
        data4 = pd.read_csv('F:\\Data cleaning\deep_learning.csv', encoding='gbk')

        data = pd.concat((pd.concat((pd.concat((data1, data2)), data3)), data4)).reset_index(drop=True)   #合并数据
        return data

    def clean_operation(self):   #将空值补充为未知
        data = self.get_data()
        data['address'] = data['address'].fillna("['未知']")
        for i, j in enumerate(data['address']):
            j = j.replace('[', '').replace(']', '')
            data['address'][i] = j
            
        for i, j in enumerate(data['salary']):  #将薪资替换为具体数值
            j = j.replace('k', '').replace('K', '').replace('以上', '-0')
            j1 = int(j.split('-')[0])
            j2 = int(j.split('-')[1])
            j3 = 1/2 * (j1+j2)
            data['salary'][i] = j3*1000
            
        for i, j in enumerate(data['industryLables']): #将行业标签上的[]去掉
            j = j.replace('[', '').replace(']', '')
            data['industryLables'][i] = j
            
        for i, j in enumerate(data['label']): #将岗位待遇字段的数据去掉[]整合
            j = j.replace('[', '').replace(']', '')
            data['label'][i] = j
         
        data['position_detail'] = data['position_detail'].fillna('未知')#将空值替换为未知

        for i, j in enumerate(data['position_detail']):#删除职位描述中的分隔符/r
            j = j.replace('\r', '')
            data['position_detail'][i] = j
            
        return data
opt = data_clean()#给清洗方法赋对象
data = opt.clean_operation()#开始清洗
print(data.head())#打印清洗好的数据
print(type(data))#查看数据类型
import os
print(os.getcwd()) #获取当前工作路径
newdata=data.to_csv('update.csv')#将清洗好的数据进导出到本地update.csv文件