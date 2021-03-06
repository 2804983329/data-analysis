#计算学员购买课程的关联性
from apriori import *
import pandas as pda
filename="D:\\Python35\\data\\lesson_buy.xls"
dataframe=pda.read_excel(filename,header=None)
#转化一下数据
change=lambda x:pda.Series(1,index=x[pda.notnull(x)])  #将该处非空转为1
mapok=map(change,dataframe.as_matrix())
data=pda.DataFrame(list(mapok)).fillna(0)
print(data)

#临界支持度、置信度设置
spt=0.2
cfd=0.5

#使用apriori算法计算关联结果
find_rule(data,spt,cfd,"-->")
