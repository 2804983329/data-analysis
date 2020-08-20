#导入数据
import pymysql
import numpy as npy
import pandas as pda
import matplotlib.pylab as pyl
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="csdn")
sql="select * from taob"
data=pda.read_sql(sql,conn)
print(data.describe())
#数据清洗
#发现缺失值
x=0
data["price"][(data["price"]==0)]=None
for i in data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j]="36"
            x+=1
print(x)
#异常值处理
#画散点图（横轴为价格，纵轴为评论数）
#得到价格
data2=data.T
price=data2.values[2]
#得到评论数据
comt=data2.values[3]
pyl.plot(price,comt,'o')
pyl.show()
#评论数异常>200000，价格异常>2300
line=len(data.values)
col=len(data.values[0])
da=data.values
for i in range(0,line):
    for j in range(0,col):
        if(da[i][2]>130):
            print(da[i][j])
            da[i][j]=36
        if(da[i][3]>300):
            print(da[i][j])
            da[i][j]=58
da2=da.T
price=da2[2]
comt=da2[3]
pyl.plot(price,comt,'o')
pyl.show()

#分布分析
pricemax=da2[2].max()
pricemin=da2[2].min()
commentmax=da2[3].max()
commentmin=da2[3].min()
#极差：最大值-最小值
pricerg=pricemax-pricemin
commentrg=commentmax-commentmin
#组距：极差/组数
pricedst=pricerg/12
commentdst=commentrg/12
#画价格的直方图
pricesty=npy.arange(pricemin,pricemax,pricedst)
pyl.hist(da2[2],pricesty)
pyl.show()
#画评论的直方图
commentsty=npy.arange(commentmin,commentmax,commentdst)
pyl.hist(da2[3],commentsty)
pyl.show()
