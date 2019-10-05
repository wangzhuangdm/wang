

#河南机电职业学院 信息工程学院
#2017级 大数据技术与应用-17-1 王壮

#导入数据清洗相关库
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')#处理报错信息
#读取本地四张CSV数据源
data1 = pd.read_csv('./data_analysis.csv', encoding='gbk')
data2 = pd.read_csv('./machine_learning.csv', encoding='gbk')
data3 = pd.read_csv('./data_mining.csv', encoding='gbk')
data4 = pd.read_csv('./deep_learning.csv', encoding='gbk')
#合并数据
data = pd.concat((pd.concat((pd.concat((data1, data2)), data3)), data4)).reset_index(drop=True)
print(data.shape) #查看数据量
print(data.head())#查看数据头五行信息

data['address'] = data['address'].fillna("['未知']")#填充缺失值为未知
data['address'][:5]#查看前五行数据
for i, j in enumerate(data['address']):        #在数据框内去除数据上的符号框[]
    j = j.replace('[', '').replace(']', '')
    data['address'][i] = j
print(data['address'][:5])

for i, j in enumerate(data['industryLables']):#在数据框内清洗岗位标签数据
    j = j.replace('[', '').replace(']', '')
    data['industryLables'][i] = j
print(data['industryLables'][:10])#查看前十条

for i, j in enumerate(data['label']):
    j = j.replace('[', '').replace(']', '')#对岗位待遇进行去括号并显示前十条
    data['label'][i] = j
print(data['label'][:10])

data['position_detail'][0].replace('\r', '')#测试去掉职位描述数据中的分隔符\r
data['position_detail'] = data['position_detail'].fillna('未知')#填充缺失值为未知
for i, j in enumerate(data['position_detail']):#在数据框下对职位描述去除分隔符\r
    j = j.replace('\r', '')
    data['position_detail'][i] = j
print(data['position_detail'][:3])#并打印前三条数据

print(data.head())#此时查看一下清洗后的前五条数据

