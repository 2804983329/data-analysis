import numpy as npy
class Bayes:
    def __init__(self):
        self.length=-1
        self.labelcount=dict()
        self.vectorcount=dict()
    def fit(self,dataSet:list,labels:list):
        if(len(dataSet)!=len(labels)):
            raise ValueError("您输入的测试数组跟类别数组长度不一致")
        self.length=len(dataSet[0])#测试数据特征值的长度
        labelsnum=len(labels)#类别所有的数量
        norlabels=set(labels)#不重复类别的数量  集合去重
        for item in norlabels:
            thislabel=item
            labelcount[thislabel]=labels.count(thislabel)/labelsnum#求的当前类别占类别总数的比例
        for vector,label in zip(dataSet,labels):
            if(label not in vectorcount):
                self.vectorcount[label]=[]
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self
    def btest(self,TestData,labelsSet):
        if(self.length==-1):
            raise ValueError("您还没有进行训练，请先训练")
        #计算testdata分别为各个类别的概率
        lbDict=dict()
        for thislb in labelsSet:
            p=1
            alllabel=self.labelcount[thislb]
            allvector=self.vectorcount[thislb]
            vnum=len(allvector)
            allvector=numpy.array(allvector).T
            for index in range(0,len(TestData)):
                vector=list(allvector[index])
                p*=vector.count(TestData[index])/vnum
            lbDict[thislb]=p*alllabel
        thislabel=sorted(lbDict,key=lambda x:lbDict[x],reverse=True)[0]
        return thislabel
