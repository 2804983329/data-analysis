import jieba
#全模式
sentence="我喜欢上海东方明珠"
w1=jieba.cut(sentence,cut_all=True)
for item in w1:
    print(item)
print("")
#精准模式
w2=jieba.cut(sentence,cut_all=False)
for item in w2:
    print(item)
print("")
#搜索引擎模式
w3=jieba.cut_for_search(sentence)
for item in w3:
    print(item)
print("")
#默认使用精准模式
w4=jieba.cut(sentence)
for item in w4:
    print(item)
print("")
#词性标注
import jieba.posseg
w5=jieba.posseg.cut(sentence)
#.flag词性
#.word词语
for item in w5:
    print(item.word+"----"+item.flag)
print("")
'''
a:形容词
c:连词
d:副词
e:叹词
f:方位词
i:成语
m:数词
n:名词
nr:人名
ns:地名
nt:机构团体
nz:其他专有名词
p:介词
r:代词
t:时间
u:助词
v:动词
vn:名动词
w:标点符号
un:未知词语
'''
#词典加载
jieba.load_userdict("D:/Python35/Lib/site-packages/jieba/dict3.txt")
sentence2="天善智能是一个很好的机构"
w6=jieba.posseg.cut(sentence2)
for item in w6:
    print(item.word+"----"+item.flag)
print("")
#修正1：add_word只能调高词频，不能调低词频，使用jieba.suggest_freq("词语",True)也一样
sentence="我喜欢上海东方明珠"
#jieba.add_word("我喜欢")
jieba.suggest_freq("我喜欢",True)
w7=jieba.cut(sentence)
for item in w7:
    print(item)
print("")
#修正2：按理来说调低词频可以使用del_word(词语)或者jieba.suggest_freq(("词1-前","词1-后"),True)，但是这里无法降低词频，有可能是电脑问题，或其他问题，各位同学也可以研究一下这个地方
'''----问题代码开始----'''
sentence="上海体育场不错的"
#jieba.del_word("上海体育场")
jieba.suggest_freq(("上海","体育场"),True)
w8=jieba.cut(sentence,)
for item in w8:
    print(item) 
'''----问题代码结束----'''

import jieba.analyse
sentence3="我喜欢上海东方明珠"
print("")
#提取关键词
tag=jieba.analyse.extract_tags(sentence3,3)
print(tag)
print("")
#返回词语的位置
w9=jieba.tokenize(sentence)
for item in w9:
    print(item)
print("")
w10=jieba.tokenize(sentence,mode="search")
for item in w10:
    print(item)
print("")

#分析血尸的词频
data=open("D:/天善Python课程/血尸.txt").read()
tag=jieba.analyse.extract_tags(data,15)
print(tag)
print("")
#盗墓笔记的关键词提取
#编码问题解决方案
#data=open("D:/天善Python课程/盗墓笔记.txt","r",encoding='utf-8').read()
import urllib.request
data=urllib.request.urlopen("http://127.0.0.1/dmbj.html").read().decode("utf-8","ignore")
tag=jieba.analyse.extract_tags(data,30)
print(tag)
