import pymysql
import pandas as pda
import numpy as npy
conn=pymysql.connect(host="127.0.0.1",user="root",passwd='root',db='csdn')
sql="select price,comment from taob"
data=pda.read_sql(sql,conn)
#离差标准化
data2=(data-data.min())/(data.max()-data.min())
#print(data2)
#标准差标准化
data3=(data-data.mean())/data.std()
#小数定标规范化
data4=data/10**(npy.ceil(npy.log10(data.abs().max())))
#print(data4)
#连续型数据离散化
#等宽离散化
data5=data[u"price"].copy()
data6=data5.T
data7=data6.values
k=3
c1=pda.cut(data7,k,labels=["便宜","适中","贵"])
#print(c1)
k=[0,50,100,300,500,2000,data7.max()]
c2=pda.cut(data7,k,labels=["非常便宜","便宜","适中","有点贵","很贵","非常贵"])
#print(c2)

#属性构造
import pymysql
import pandas as pda
import numpy as npy
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="hexun")
sql="select * from myhexun"
data8=pda.read_sql(sql,conn)
#print(data8)
ch=data8[u"comment"]/data8["hits"]
data8[u"评点比"]=ch
file="./hexun.xls"
#data8.to_excel(file,index=False)

#主成分分析
from sklearn.decomposition import PCA
import pymysql
import pandas as pda
import numpy as npy
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="hexun")
sql="select hits,comment from myhexun"
data9=pda.read_sql(sql,conn)
ch=data9[u"comment"]/data8["hits"]
data9[u"评点比"]=ch
#--主成分分析进行中--
pca1=PCA()
pca1.fit(data9)
#返回模型中各个特征量
Characteristic=pca1.components_
#print(Characteristic)
#各个成分中各自方差百分比，贡献率
rate=pca1.explained_variance_ratio_
#print(rate)

pca2=PCA(2)
pca2.fit(data9)
reduction=pca2.transform(data9)#降维
print(reduction)
recovery=pca2.inverse_transform(reduction)#恢复
print(recovery)




