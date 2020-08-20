#kmeans算法
#通过程序实现录取学生的聚类
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
fname="D:\\Python35\\data\\luqu.csv"
dataf=pda.read_csv(fname)
x=dataf.iloc[:,1:4].as_matrix()
#from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=2)
#kms=KMeans(n_clusters聚多少类=2，n_jobs线程数=2，max_iter最多循环数=500)
y=kms.fit_predict(x) #进行聚类
print(y)
#x代表学生序号，y代表学生类别
s=npy.arange(0,len(y))
pyl.plot(s,y,"o")
pyl.show()
#通过程序实现商品的聚类
import pandas as pda
import numpy as npy
import matplotlib.pylab as pyl
import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="tb")
sql="select price,comment from goods limit 300"
dataf=pda.read_sql(sql,conn)
x=dataf.iloc[:,:].as_matrix()
#from sklearn.cluster import Birch
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=2)
y=kms.fit_predict(x)
print(y)
for i in range(0,len(y)):
    if(y[i]==0):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*r")
    elif(y[i]==1):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"sy")
    elif(y[i]==2):
        pyl.plot(dataf.iloc[i:i+1,0:1].as_matrix(),dataf.iloc[i:i+1,1:2].as_matrix(),"*k")
pyl.show()
#作业:使用聚类来实现文本的聚类
#1、用爬虫去爬100个百度百科的词条内容
#2、将这些内容分别存入各文件中
#3、进行分词，计算tf-idf
#4、进行聚类
#5、对文档进行归类

