#决策树
import pandas as pda
fname="D:\\Python35\\data\\lesson.csv"
dataf=pda.read_csv(fname,encoding="gbk")
x=dataf.iloc[:,1:5].as_matrix()
y=dataf.iloc[:,5].as_matrix()
for i in range(0,len(x)):
    for j in range(0,len(x[i])):
        thisdata=x[i][j]
        if(thisdata=="是" or thisdata=="多" or thisdata=="高"):
            x[i][j]=int(1)
        else:
            x[i][j]=-1
for i in range(0,len(y)):
    thisdata=y[i]
    if(thisdata=="高"):
        y[i]=1
    else:
        y[i]=-1
#容易错的地方:直接dtc训练
#正确的做法：转化好格式，将x，y转化为数据框，然后再转化为数组并指定格式
xf=pda.DataFrame(x)
yf=pda.DataFrame(y)
x2=xf.as_matrix().astype(int)
y2=yf.as_matrix().astype(int)
#建立决策树
from sklearn.tree import DecisionTreeClassifier as DTC
dtc=DTC(criterion="entropy") #设置为信息熵模式
dtc.fit(x2,y2)
#直接预测销量高低
import numpy as npy
x3=npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst=dtc.predict(x3)
print(rst)
#可视化决策树
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("D:\\我的教学\\Python\\天善-Python数据分析+爬虫\dtc.dot","w") as file:
    export_graphviz(dtc,feature_names=["combat","num","Promotion","datum"],out_file=file)


#导出DTC。dot文件后可以使用工具软件转为pdf或其他格式文件





