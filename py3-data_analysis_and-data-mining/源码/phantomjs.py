from selenium import webdriver
import time
import re
from lxml import etree
bs=webdriver.PhantomJS()
time.sleep(3)
url="http://s.weibo.com/weibo/%25E4%25BD%259F%25E4%25B8%25BD%25E5%25A8%2585%2520%25E5%259B%259E%25E5%25BA%2594?topnav=1&wvr=6&Refer=top_hot"
bs.get(url)
bs.get_screenshot_as_file("D:/Python35/test.jpg")
data=bs.page_source
#pattitle="<title>(.*?)</title>"
#title=re.compile(pattitle).findall(data)
#print(title)
#如何在urllib或者phantomjs中使用xpath表达式
#要将data转为tree，再进行xpath提取即可
'''
edata=etree.HTML(data)
title2=edata.xpath("/html/head/title/text()")
print(title2)
'''
#提取微博发布者
patnick='nick-name="(.*?)"'
nickname=re.compile(patnick).findall(data)
print(nickname)
#去掉em标签
patem='<em class="red">.*?</em>'
cp1=re.compile(patem)
dataem=re.sub(cp1,"",data)
#去掉img标签
patimg='<img.*?>'
cp2=re.compile(patimg)
dataimg=re.sub(cp2,"",dataem)
#提取微博内容
patweibo='<p class="comment_txt".*?>(.*?)<a'
weibo=re.compile(patweibo,re.S).findall(dataimg)
print(weibo)
fh=open("D:/Python35/test.html","wb")
fh.write(data.encode("utf-8"))
fh.close()
bs.quit()
#课后自己研究一下：1、如何使用phantomjs定位元素，以及进行点击，数据清除等操作
#2、如何使用phantomjs提交表单

#文本分类（情感分析）
#加载文本
#将文本转为特征矩阵（*）
#构建算法
#分好训练数据和测试数据
#对数据进行训练
#对数据进行预测（测试）
num=len(weibo)
trainnum=int(num*0.5)
'''
tlabels=[]
for i in range(0,trainnum):
    print("第"+str(i)+"条微博为"+weibo[i])
    thislabels=input("请输入微博情感类别：1正向，0负向，2为中性")
    tlabels.append(thislabels)
print(tlabels)
'''
#微博切词
import jieba
cutdata=[]
for i in range(0,num):
    thisdata=weibo[i]
    thiscut=jieba.cut(thisdata)
    thiscutdata=""
    for j in thiscut:
        thiscutdata=thiscutdata+j+" "
    cutdata.append(thiscutdata)

from sklearn.feature_extraction.text import CountVectorizer
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(cutdata)
alltz=x.toarray()
#获取训练数据矩阵
trainlabels=['2', '2', '2', '2', '1', '1', '1', '0', '0', '1']
traindata=alltz[0:trainnum,:]

#构建模型（KNN、贝叶斯、人工神经网络、决策树）

#测试数据
testdata=alltz[trainnum:,:]
print(testdata)

#大家回去先尝试做：
#1、尝试登陆微博（phantomjs），然后爬取更多微博数据
#2、构建模型（自己喜欢的算法）
#3、训练数据
#4、测试数据
#然后我们在17或18号中午给大家讲解



























