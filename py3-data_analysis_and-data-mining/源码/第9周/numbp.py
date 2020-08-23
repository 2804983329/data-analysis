#使用人工神经网络实现手写体数字识别
#数据的读取与整理
#加载数据
from numpy import *
import operator
from os import listdir
import numpy as npy
import pandas as pda
import numpy
def datatoarray(fname):
    arr=[]
    fh=open(fname)
    for i in range(0,32):
        thisline=fh.readline()
        for j in range(0,32):
            arr.append(int(thisline[j]))
    return arr
#建立一个函数取文件名前缀
def seplabel(fname):
    filestr=fname.split(".")[0]
    label=int(filestr.split("_")[0])
    return label
#建立训练数据
def traindata():
    labels=[]
    trainfile=listdir("D:/Python35/traindata")
    num=len(trainfile)
    #长度1024（列），每一行存储一个文件
    #用一个数组存储所有训练数据，行：文件总数，列：1024
    trainarr=zeros((num,1024))
    for i in range(0,num):
        thisfname=trainfile[i]
        thislabel=seplabel(thisfname)
        labels.append(thislabel)
        trainarr[i,:]=datatoarray("D:/Python35/traindata/"+thisfname)
    return trainarr,labels
trainarr,labels=traindata()
xf=pda.DataFrame(trainarr) #转为数据框格式：一种表格型数据结构
yf=pda.DataFrame(labels)
tx2=xf.as_matrix().astype(int) #设置类型为int格式
ty2=yf.as_matrix().astype(int)

#使用人工神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense,Activation
model=Sequential()
#输入层
model.add(Dense(10,input_dim=1024))  #设置为tx2的维度   数据形状shape(a,b)  a是记录数 b是维度   一般使用便变量方式 如input_dim=len(tx2[0]）  tx2第0层的维度
model.add(Activation("relu"))
#输出层
model.add(Dense(1,input_dim=1))
model.add(Activation("sigmoid"))
#模型的编译
model.compile(loss="mean_squared_error",optimizer="adam")  #mean_squared_error 均方误差  和  binary_crossentropy 二分类
#训练
model.fit(tx2,ty2,nb_epoch=10000,batch_size=6)
#预测分类
rst=model.predict_classes(x).reshape(len(x))
x=0
for i in range(0,len(x2)):
    if(rst[i]!=y[i]):
        x+=1
print(1-x/len(x2))
import numpy as npy
x3=npy.array([[1,-1,-1,1],[1,1,1,1],[-1,1,-1,1]])
rst=model.predict_classes(tx2).reshape(len(tx2))
print(rst)

#20200823