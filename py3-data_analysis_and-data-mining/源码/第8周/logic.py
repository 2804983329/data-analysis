import pandas as pda
fname="D:/Python35/data/luqu.csv"
dataf=pda.read_csv(fname)
x=dataf.iloc[:,1:4].as_matrix()  #获取所有行（：），列获取1到4
y=dataf.iloc[:,0:1].as_matrix() #获取第0列   as_matrix()转为数组
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR
r1=RLR()
r1.fit(x,y)
r1.get_support()#特征筛选
#print(dataf.columns[r1.get_support()])
t=dataf[dataf.columns[r1.get_support()]].as_matrix()
r2=LR()
r2.fit(t,y)
print("训练结束")
print("模型正确率为:"+str(r2.score(x,y)))
