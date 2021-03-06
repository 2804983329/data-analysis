## 1.生成数据表
### 导入相关库
```python
import numpy as np
import pandas as pd
```

### 导入数据表   
导入数据表的可以从excel或csv格式文件导入数据并创建数据表。代码可设置参数有：列名称、索引列、数据格式等   
```python
df=pd.DataFrame(pd.read_csv('name.csv',header=1))
df=pd.DataFrame(pd.read_excel('name.xlsx'))
```

### 创建数据表   
另一种方法是通过直接写入数据来生成数据表，excel 中直接在单元格中输入数据就可以，python 中通过下面的代码来实现。生成数据表的函数是 pandas 库中的 DateFrame 函数，数据表一共有 6 行数据，每行有 6 个字段。在数据中我们特意设置了一些 NA 值和有问题的字段，例如包含空格等。后面将在数据清洗步骤进行处理。后面我们将统一以 DataFrame 的简称 df 来命名数据表。

```python
df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
                   "date":pd.date_range('20130102', periods=6),
                   "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
                   "age":[23,44,54,32,34,32],
                   "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
                   "price":[1200,np.nan,2133,5433,np.nan,4432]},
                   columns =['id','date','city','category','age','price'])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/%E5%88%9B%E5%BB%BA%E6%95%B0%E6%8D%AE%E8%A1%A8.jpg)


## 02 数据表检查   
第二部分是对数据表进行检查，python 中处理的数据量通常会比较大，比如我们之前的文章中介绍的纽约出租车数据和 Citibike 的骑行数据，数据量都在千万级，我们无法一目了然的 了解数据表的整体情况，必须要通过一些方法来获得数据表的关键信息。数据表检查的另一个目的是了解数据的概况，例如整个数据表的大小，所占空间，数据格式，是否有空值和重复项和具体的数据内容。为后面的清洗和预处理做好准备。    

### 数据维度（行列）   

Excel中可以通过CTRL + 向下的光标键，和CTRL + 向右的光标键来查看行号和列号。Python中使用shape函数来查看数据表的维度，也就是行数和列数，函数返回的结果（6，6）表示数据表有6行，6列。具体代码如下：
```python
#查看数据表的维度
df.shape
(6,6)
```

### 数据表信息   

使用info函数查看数据表的整体信息，这里返回的信息较多（其中包含数据维度，列名称， 数据格式和所占空间等信息）
```python
1#数据表信息
 2df.info()
 3
 4&lt;class 'pandas.core.frame.DataFrame'&gt;
 5RangeIndex: 6 entries, 0 to 5
 6Data columns (total 6 columns):
 7id          6 non-null int64
 8date        6 non-null datetime64[ns]
 9city        6 non-null object
10category    6 non-null object
11age         6 non-null int64
12price       4 non-null float64
13dtypes: datetime64[ns](1), float64(1), int64(2), object(2)
14memory usage: 368.0+ bytes
```

### 查看数据格式     
Excel中通过选中单元格并查看开始菜单中的数值类型来判断数据的格式。Python中使用dtypes函数来返回数据格式
![image](https://github.com/2804983329/data-analysis/blob/master/picture/excel查看格式.jpg)
Dtypes是一个查看数据格式的函数，可以一次性查看数据表中所有数据的格式，也可以指定一列来单独查看。
```python
#查看数据表各列格式
 df.dtypes
 
 id                   int64
 date        datetime64[ns]
 city                object
 category            object
 age                  int64
 price              float64
 dtype: object

#查看单列格式
df['B'].dtype

dtype('int64')
```

### 查看空值   
Excel中查看空值的方法是使用 “定位条件” 功能对数据表中的空值进行定位。“定位条件”在“开始”目录下的“查找和选择”目录中。
Isnull 是Python中检查空值的函数，返回的结果是逻辑值，包含空值返回True，不包含则返回False。可以对整个数据表进行检查，也可以单独对某一列进行空值检查。
```python
#检查数据空值
df.isnull()
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/jianchashujukongzhi.jpg)

```python
#检查特定列空值
df['price'].isnull()

 0    False
 1     True
 2    False
 3    False
 4     True
 5    False
10Name: price, dtype: bool
```

### 查看唯一值   
Excel中查看唯一值的方法是使用 “条件格式” 对唯一值进行颜色标记。 Python中使用unique函数查看唯一值。   
Unique是查看唯一值的函数，只能对数据表中的特定列进行检查。下面是代码，返回的结果是该列中的唯一值。类似于Excel中删除重复项后的结果。
```python
#查看 city 列中的唯一值
df['city'].unique()

array(['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '], dtype=object)
```

### 查看数据表数值   
Python中的Values函数用来查看数据表中的数值。以数组的形式返回，不包含表头信息。

```python
#查看数据表的值
df.values

array([[1001, Timestamp('2013-01-02 00:00:00'), 'Beijing ', '100-A', 23,
         1200.0],
        [1002, Timestamp('2013-01-03 00:00:00'), 'SH', '100-B', 44, nan],
        [1003, Timestamp('2013-01-04 00:00:00'), ' guangzhou ', '110-A', 54,
         2133.0],
        [1004, Timestamp('2013-01-05 00:00:00'), 'Shenzhen', '110-C', 32,
        5433.0],
       [1005, Timestamp('2013-01-06 00:00:00'), 'shanghai', '210-A', 34,
        nan],
       [1006, Timestamp('2013-01-07 00:00:00'), 'BEIJING ', '130-F', 32,
        4432.0]], dtype=object)
```

### 查看列名称   

Column函数用来单独查看数据表中的列名称

```
#查看列名称
df.columns

 Index(['id', 'date', 'city', 'category', 'age', 'price'], dtype='object')
```


### 查看前10行数据
Head函数用来查看数据表中的前N行数据，默认head()显示前10行数据，可以自己设置参数值来   
确定查看的行数。查看前三行数据的代码如下   
```
#查看前3行数据
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chakanqiansanhangshuju.jpg)

### 查看后数据    
tail函数和head函数相反，用来查看数据表中后N行的数据，   
可以自己设置参数值来确定查看的行数。查询后三行示例如下：    
```
#查看最后三行
df.tail(``3``)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chakanhousanhang.jpg)


## 03数据表清洗
第三部分是对数据表中的的问题进行清洗。主要内容包括对空值，大小写问题，数据格式和重复值的处理。   
不包含对数据间的逻辑验证。   

### 处理空值（删除或填充）   
我们在创建数据表的时候在price字段中故意设置几个NA值。对于空值的处理方式
有很多种，可以直接删除包含空值的数据，也可以对空值进行填充，比如用0填充或者用
均值填充。还可以根据不同字段的逻辑对空值进行推算。

excel 中可以通过“查找和替换” 功能对空值进行处理，将空值统一替换为0或均值
。也可以通过定位空值来实现。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chakanhousanhang.jpg)


Python中处理空值的方法比较灵活，可以使用Dropna函数用来删除数据表中包含空值的数据
，也可以使用fillna函数对空值进行填充。下面代码和结构中可以看到使用dropna函数后，
包含NA值的两个字段已经不见了。返回的是一个不包含空值的数据表。
```
#删除数据表中含有空值的行
df.dropna(how='any')
```

![image](https://github.com/2804983329/data-analysis/blob/master/picture/chulikongzhi2.jpg)


除此之外也可以使用数字对空值进行填充，下面的代码使用fillna函数对空值字段填充数字0
```python
#使用数字 0 填充数据表中的空值
df.fillna(value=0)
```

我们选择填充的方式来处理空值，使用price列的均值来填充NA字段，统一使用fillna函数，早要填充的数值中使用mean函数先计算price列当前的均值，然后使用这个均值对NA进行填充。可以看到两个空值字段显示为3299.5
```python
#使用price 均值对na进行填充
df['price'].fillna(df['price'].mean())

0    1200.0
1    3299.5
2    2133.0
3    5433.0
4    3299.5
5    4432.0
Name: price, dtype: float64
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chulikongzhi3.jpg)

### 清理空格    
除了空值，字符中的空格也是数据清洗中一个常见的问题，
```python
#清除 city字段找那个的的字符空格
df['city']=df['city'].map(str.strip)
```

### 大小写转换   
在 英文字段汇总，字母的大小写不统一也是一个常见的问题，Excel中有UPPER，LOWER等函数，python中也有同名函数来解决大小写的问题。在数据表的city列中就存在这样的问题，我们将city列中的所有字母转换成小写。代码如下：
```python
#city 列大小写转换
df['city']=df['city'].str.lower()
```

![image](https://github.com/2804983329/data-analysis/blob/master/picture/daxiaoxiezhuanhuan1.jpg)   


### 更改数据格式   
Excel中通过“设置单元格格式”功能可以修改数据格式，python中通过astype函数来修改数据格式

![image](https://github.com/2804983329/data-analysis/blob/master/picture/genggaishujugeshi1.jpg)   

python中查看数据格式的函数是dtype，与之对应的是astype函数，用来更高数据格式，下面的代码中将price字段的值修改成int格式。
```python
#更改数据格式
df['price'].astype('int')

0    1200
1    3299
2    2133
3    5433
4    3299
5    4432
Name: price, dtype: int32
```

### 更改列名称    
Rename是更改列名称的函数，我们将数据表中的category列更改为category-size。下面是具体的代码和更改后的结果
```python
#更改列名称
df.rename(columns={'category': 'category-size'})
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/genggailiemingcheng1.jpg) 

### 删除重复值   
很多数据表中还包含重复值的问题，Excel 的数据目录下有“删除重复项”的功能，可以用来删除数据表中的重复值。默认 Excel 会保留最先出现的数据，删除后面重复出现的数据。   
Python 中使用 drop_duplicates 函数删除重复值。我们以数据表中的 city 列为例，city 字段中存在重复值。默认情况下 drop_duplicates()将删除后出现的重复值(与 excel 逻辑一致)。增加 keep=’last’参数后将删除最先出现的重复值，保留最后的值。下面是具体的代码和比较结果。

原始的 city 列中 beijing 存在重复，分别在第一位和最后一位。
```python
df['city']
0      beijing
1           sh
2    guangzhou
3     shenzhen
4     shanghai
5      beijing
Name: city, dtype: object
```
使用默认的 drop_duplicates()函数删除重复值，从结果中可以看到第一位的 beijing 被保留，最后出现的 beijing 被删除。
```python
#删除后出现的重复值
df['city'].drop_duplicates()
0       beijing
1           sh
2    guangzhou
3     shenzhen
4     shanghai

Name: city, dtype: objec
```
设置 keep=’last‘’参数后，与之前删除重复值的结果相反，第一位出现的 beijing 被删除，保留了最后一位出现的 beijing。
```python
#删除先出现的重复值
df['city'].drop_duplicates()
1           sh
2    guangzhou
3     shenzhen
4     shanghai
5      beijing
Name: city, dtype: objec
```

### 数值修改及替换    
数据清洗中最后一个问题是数值修改或替换，Excel中使用“查找和替换”功能就可以实现数值的替换。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chazhaojitihuan.jpg) 
Python中使用replace函数实现数据替换。数据表中city字段上还存在两种写法，分别为shanghai和SH。我们使用replace函数对SH进行替换。
```python
#数据替换
df['city'].replace('SH','shanghai')
0      beijing
1     shanghai
2    guangzhou
3     shenzhen
4     shanghai
5      beijing
Name: city, dtype: object
```

本篇文章这是系列的第二篇，介绍第4——6部分的内容，数据表的生成，数据表的查看，和数据清洗。

![image](https://github.com/2804983329/data-analysis/blob/master/picture/mulu2.jpg) 
## 数据预处理    
第四部分是数据的预处理，对清洗完的数据进行整理仪表后期的统计和分析工作，主要包括数据表的合并、排序、数据分裂、数据分组、标记等工作。
### 数据表合并   
首先是对不同的数据表进行合并，我们这里创建一个新的数据表df1，并将df和df1两个数据表进行合并。在Excel中没有直接完成数据表合并的功能，可以通过VLOOKUP函数分步实现，在python中可以通过merge函数一次性实现，下面建立df1数据表，用于和df数据表进行合并。
```python
#创建 df1 数据表
df1=pd.DataFrame({"id":[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
"gender":['male','female','male','female','male','female','male','female'],
"pay":['Y','N','Y','Y','N','Y','N','Y',],
"m-point":[10,12,20,40,40,40,30,20] })
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chuangjianshujubiao1.jpg) 
使用merge函数对两个数据表进行合并，合并方式为inner，将两个数据表中共有的数据匹配到一起生成新的数据表。并命名为df_inner.
```python
#数据表匹配合并，inner 模式
df_inner=pd.merge(df,df1,how='inner')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujubiaohebing-inner.jpg) 

除了inner方式以外，合并的方式还有left， right和outer方式，
```python
#其他数据表匹配模式
df_left=pd.merge(df,df1,how='left')
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')
```

### 设置索引列   
完成数据表的合并后，我们对 df_inner 数据表设置索引列，索引列的功能很多，可以进行数据提取，汇总，也可以进行数据筛选等。
设置索引的函数为 set_index。
```python
#设置索引列
df_inner.set_index('id')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shezhisuoyinlie.jpg) 

### 排序(按索引，按数值)
Excel 中可以通过数据目录下的排序按钮直接对数据表进行排序，比较简单。Python 中需要使用 ort_values 函数和 sort_index 函数完成排序。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/paixu1.jpg) 
在 python 中，既可以按索引对数据表进行排序，也可以看制定列的数值进行排序。首先我们按 age 列中用户的年龄对数据表进行排序。
使用的函数为 sort_values。
```python
#按特定列的值排序
df_inner.sort_values(by=['age'])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/paixu2.jpg) 
Sort_index函数用来将数据表按索引列的值进行排序。
```python
#按索引列排序
df_inner.sort_index()
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/ansuoyinliepaixu1.jpg) 

### 数据分组
Excel 中可以通过 VLOOKUP 函数进行近似匹配来完成对数值的分组，或者使用“数据透视表”来完成分组。相应的 python 中使用 where 函数完成数据分组。

Where 函数用来对数据进行判断和分组，下面的代码中我们对 price 列的值进行判断，将符合条件的分为一组，不符合条件的分为另一组，并使用 group 字段进行标记。
```python
#如果 price 列的值>3000，group 列显示 high，否则显示 low
df_inner['group'] = np.where(df_inner['price'] > 3000,'high','low')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujufenzu1.jpg) 
除了 where 函数以外，还可以对多个字段的值进行判断后对数据进行分组，下面的代码中对 city 列等于 beijing 并且 price 列大于等于 4000 的数据标记为 1。
```python
#对复合多个条件的数据进行分组标记
df_inner.loc[(df_inner['city'] == 'beijing') & (df_inner['price'] >= 4000), 'sign']=1
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/duifuhetiaojiandeshujujinxingfenzu.jpg) 

### 数据分列
与数据分组相反的是对数值进行分列，Excel中的数据目录下提供“分列”功能，在python中使用split函数实现分列。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/Excelfenlie.jpg) 
在数据表中 category 列中的数据包含有两个信息，前面的数字为类别 id，后面的字母为 size 值。中间以连字符进行连接。我们使用 split 函数对这个字段进行拆分，并将拆分后的数据表匹配回原数据表中。
```python
#对 category 字段的值依次进行分列，并创建数据表，索引值为 df_inner 的索引列，列名称为 category 和 size
pd.DataFrame((x.split('-') for x in df_inner['category']),index=df_inner.index,columns=['category','size'])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/pythonfenlie.jpg)
```python
#将完成分列后的数据表与原 df_inner 数据表进行匹配
df_inner=pd.merge(df_inner,split,right_index=True, left_index=True)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujubiaopipei.jpg) 

## 05 数据提取
数据提取主要通过使用三个函数（loc、iloc、和ix）来进行的，其中loc函数按照标签值进行提取，iloc按照位置进行提取，ix可以同时按标签和位置进行提取。
### 按标签提取（loc）   
Loc函数按数据表的索引标签进行提取，如下提取索引列为3的单条数据
```python
#按索引提取单行的数值
df_inner.loc[3]
id 1004
date 2013-01-05 00:00:00
 city shenzhen
 category 110-C
 age 32
 price 5433
 gender female
m-point 40
pay Y
group high
sign NaN
category_1 110
size C
Name: 3, dtype: object
```
使用冒号可以限定提取数据的范围，冒号前面为开始的标签值，后面为结束的标签值，如下提取了0到5的数据行
```python
#按索引提取区域行数值
df.inner.loc[0:5]
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/tiququyuhangshuzhi.jpg) 
Reset_index函数用于恢复索引，此处重新将date字段的日期设置为数据表的索引，并按日期进行数据提取。

```python
#重设索引
df_inner.reset_index()
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chongshesuoyin.jpg) 
```python
#设置日期为索引
df_inner=df_inner.set_index('date')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shezhiriqiweisuoyin.jpg) 
使用冒号限定提取数据的范围，冒号前面为空表示从0开始。提取所有2013年1月4日以前的数据。
```python
#提取4日之前的所有数据
df_inner[:'2013-01-04']
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/tiqusiriqiansuoyoushuju.jpg) 

### 按位置提取（iloc）
使用iloc函数按位置对数据表中的数据进行提取，这里的冒号前后的数字不再是索引的标签名称，而是数据所在的位置，从0开始。
```python
#使用iloc按位置区域提取数据
df_inner.iloc(:3,:2)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/iloc1.jpg) 
iloc函数除了可以按区域提取数据，还可以按位置逐条提取，前面方括号中的0，2，5表示数据所在行的位置，后面方括号中的数表示所在列的位置。
```python
#使用iloc按位置单独提取数据
df_inner.iloc[[0,2,5],[4,5]]
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/iloc2.jpg) 
### 按标签和位置提取（ix）   
ix是loc和iloc的混合，既能按索引标签提取，也能按位置进行数据提取。下面代码中行的位置按索引日期设置，列按位置设置。

```python
#使用ix按索引标签额位置混合提取数据
df_inner.ix[:'2013-01-03',4]
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/ix1.jpg) 
### 按条件提取（区域和条件值）
除了按标签和位置提取数据外，还可以按具体的条件进行数据提取。下面使用loc和isin两个函数配合使用，按指定条件对数据进行提取。
使用isin函数对city中的值是否为beijing进行判断。
```python
#判断city列的值是否为beijing
df_inner['city'].isin(['beijing'])

 date
 2013-01-02 True
 2013-01-05 False
 2013-01-07 True
 2013-01-06 False
 2013-01-03 False
2013-01-04 False
Name: city, dtype: bool
```
將isin函数嵌套到loc的数据提取函数中，将判断结果为True数据提取出来。这里把判断条件改为city值是否为beijing和shanghai。如果是就把这条数据提取出来。

```python
#先判断city列里是否包含beiijing和shanghai，然后将符合条件的数据提取出来
df_inner.loc[df_inner['city'].isin(['beijing','shanghai'])]
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/tiaojiantiqu1.jpg) 
数据提取还可以完成类似数据分列的广州，从合并的数值中提取出指定的数值

```python
categroy=df_inner['categroy']
 0 100-A
 3 110-C
 5 130-F
 4 210-A
 1 100-B
 2 110-A
 Name: category, dtype: object
 
#提取前三个字符，并生成数据表
pd.Dataframe(categrop.str[:3])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujutiqufenlie.png)


## 06 数据筛选   
数据筛选：通过使用与，或，非三个天骄配合大于，小于和等于对数据进行筛选，并进行计数和求和。与excel中的筛选功能和countifs和sumifs功能相似。


### 按条件筛选（与，或，非）   
Excel 数据目录下提供了“筛选”功能，用于对数据表按不同的条件进行筛选。Python 中使用 loc 函数配合筛选条件来完成筛选功能。配合 sum 和 count 函数还能实现 excel 中 sumif 和 countif 函数的功能。

![image](https://github.com/2804983329/data-analysis/blob/master/picture/excel-tiaojianshaixuan.jpg) 
使用“与”条件进行筛选，年龄大于25岁，并且城市为beijing。筛选后只有一条数据符合要求
```python
#使用“与”条件进行筛选
df_inner.loc[(df_inner['age'] > 25) & (df_inner['city'] == 'beijing'),['id','city','age','categroy','gender']]
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/yutiaojianshaixuan.jpg) 
使用“或”条件进行筛选，年龄大于25岁或城市为beijing。筛选后有6条数据符合要求
```python
#使用“或”条件筛选
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'),['id','city','age','category','gender']].sort(['age'])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/huotiaojianshaixuan.jpg) 
在前面的代码后增加price字段以及sum函数，按筛选后的结果将price字段值进行求和，相当于excel中sumifs的功能
```python
#对筛选后的数据按price字段进行求和
df_inner.loc[(df_inner['age'] > 25) | (df_inner['city'] == 'beijing'),['id','city','age','category','gender','price']].sort(['age']).price.sum()

```
使用“非”条件进行筛选，城市不等于beijing。符合条件的数据有4条。将筛选结果按id列进行排序。
```python
#使用“非”条件进行筛选
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id'])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/feitiaojianshaixuan.jpg) 
在前面的代码后面增加city列，并用count函数进行计数，相当于excel中的countifs函数的功能。
```python
#对筛选后的数据按 city 列进行计数
df_inner.loc[(df_inner['city'] != 'beijing'), ['id','city','age','category','gender']].sort(['id']).city.count()

```
还有一种筛选的方式是用query函数。下面是具体的代码和筛选结果。
```python
使用 query 函数进行筛选
df_inner.query('city == ["beijing", "shanghai"]')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/queryhanshushaixuan.jpg) 
在前面的代码后增加 price 字段和 sum 函数。对筛选后的 price 字段进行求和，相当于 excel 中的 sumifs 函数的功能。
```python
#对筛选后的结果按 price 进行求和
df_inner.query('city == ["beijing", "shanghai"]').price.sum()
```
以下是第三篇，介绍第 7-9 部分的内容，数据汇总，数据统计，和数据输出。

## 07 数据汇总   
第七部分是对数据进行分类汇总，Excel中使用分类汇总和数据透视可以按特定维度对数据进行汇总，python中使用的主要函数是groupby 和 privot_tabel。下面分别介绍两个函数

### 分类汇总   
Excel的数据目录下提供了“分类汇总”功能，可以按指定的字段和汇总方式对数据表进行汇总。python中通过Groupby函数完成相应的操作，并且可以支持多级分类汇总。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/fenleihuizong1.jpg) 
Groupby是进行分类汇总的函数，使用方法简单，制定要分组的列名称就可以，也可以同时制定多个列名称，groupby按列名称出现的顺序进行分组。同时要制定分组后的汇总方式，常见的是计数和求和两种
```python
#对所有的列进行计数汇总
df_inner.groupby('city').count()
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/fenleihuizong2.jpg) 

可以在groupby中设置列名称来对特定的列进行汇总。下面的代码中按城市对id字段进行汇总计数。
```python
#对特定的ID列进行计数汇总
df_inner.groupby('city')['id'].count()
city
beijing 2
guangzhou 1
shanghai 2
shenzhen 1
Name: id, dtype: int64
```
在前面的基础上增加第二个列名称，分别对city 和size 两个字段进行计数汇总。
```python
#对两个字段进行汇总计数
df_inner.groupby(['city','size'])['id'].count()
city size
beijing A 1
F 1
guangzhou A 1
shanghai A 1
B 1
shenzhen C 1
Name: id, dtype: int64
```
除了计数和求和外，还可以对汇总后的数据同时按多个维度进行计算，下面的的代码中按城市对price字段进行汇总，并分别计算price的数量，总金额和平均金额。
```python
#对 city 字段进行汇总并计算 price 的合计和均值。
df_inner.groupby('city')['price'].agg([len,np.sum, np.mean])
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/fenleihuizong3.jpg) 

### 数据透视   
Excel中的插入目录下提供“数据透视表”功能对数据表按特定维度进行汇总。python中也提供了数据透视表功能。通过pivot_table函数实现同样的效果。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujutoushi1.jpg) 
数据透视表也是常用的一种数据分类汇总方式，并且功能上比groupby要强大一些，下面的代码中设定city为行字段，size为列字段，price为值字段，分别计算price的数量和金额并且按行与列进行汇总。
```python
#数据透视表
pd.pivot_table(df_inner,index=["city"],values=["price"],columns=["size"],aggfunc=[len,no.sum],fill_value=0,margins=True)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujutoushi2.jpg) 


## 08 数据统计   
第九部分为数据统计，这里主要介绍数据采样，标准差，协方差和相关系数的使用方法。

### 数据采样   

Excel的数据分析功能中提供了数据抽样的功能，如下图所示。python通过sanple函数完成数据采样。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang1.jpg) 

sample是进行数据采样的函数，设置n的数量就可以了。函数自动返回采样的结果。
```python
#简单的数据采样
df_inner.sample(n=3)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang2.jpg) 
Weightscan 参数是采样的权重，通过设置不同的权重可以更高采样的结果，权重高的数据将更有希望被选中，这里手动设置6条数据的权重值，将前面的4个设置为0，后面的两个设置为0.5。

```python
#手动设置采样权重
weights = [0, 0, 0, 0, 0.5, 0.5]
df_inner.sample(n=2, weights=weights)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang3.jpg) 
从采样的结果可以看出，后面两条权重高的数据被选中。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang4.jpg) 

sample函数还有一个参数replace，用来设置采样后是否放回。
```python
#采样后不放回
df_inner.sample(n=6, replace=False)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang5.jpg) 
```python
#采样后放回
df_inner.sample(n=6, replace=True)
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujucaiyang6.jpg) 

### 描述统计
Excel中的数据分析中提供了描述统计的功能吗。python中可以通过Describe对数据进行描述统计。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/miaoshutongji1.jpg) 

Describe 函数是进行描述统计的函数，自动生成数据的数量，均值，标准差等数据。下面的代码中对数据表进行描述统计，并使用 round 函数设置结果显示的小数位。并对结果数据进行转置。

```python
#数据表描述性统计
df_inner.describe().round(2).T
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/shujubiaomiaoshuxingtongji1.jpg) 
#### 标准差
Python 中的 Std 函数用来接算特定数据列的标准差。
```python 
#标准差
df_inner['price'].std()
1523.3516556155596
```

#### 协方差 

Excel 中的数据分析功能中提供协方差的计算，python 中通过 cov 函数计算两个字段或数据表中各字段间的协方差。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/xiefangcha1.jpg) 

Cov 函数用来计算两个字段间的协方差，可以只对特定字段进行计算，也可以对整个数据表中各个列之间进行计算。
```python
#两个字段间的协方差
df_inner['price'].cov(df_inner['m-point'])
17263.200000000001
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/xiefangcha2.jpg) 

#### 相关分析   
Excel 的数据分析功能中提供了相关系数的计算功能，python 中则通过 corr 函数完成相关分析的操作，并返回相关系数。
![image](https://github.com/2804983329/data-analysis/blob/master/picture/xiangguangfenxi1.jpg) 

Corr 函数用来计算数据间的相关系数，可以单独对特定数据进行计算，也可以对整个数据表中各个列进行计算。相关系数在-1 到 1 之间，接近 1 为正相关，接近-1 为负相关，0 为不相关。
```python
#相关性分析
df_inner['price'].corr(df_inner['m-point'])
0.77466555617085264

#数据表相关性分析
df_inner.corr()
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/xiangguangfenxi2.jpg) 


## 09 数据输出

第九部分是数据输出，处理和分析完的数据可以输出为 xlsx 格式和 csv 格式。

写入 excel
```python
#输出到 excel 格式
df_inner.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc')
```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/xieruexcel1.jpg) 

写入 csv
```python
#输出到 CSV 格式
df_inner.to_csv('excel_to_python.csv')
```

在数据处理的过程中，大部分基础工作是重复和机械的，对于这部分基础工作，我们可以使用自定义函数进行自动化。以下简单介绍对数据表信息获取自动化处理。
```python
 #创建数据表
 df = pd.DataFrame({"id":[1001,1002,1003,1004,1005,1006],
 "date":pd.date_range('20130102', periods=6),
 "city":['Beijing ', 'SH', ' guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
 "age":[23,44,54,32,34,32],
 "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
 "price":[1200,np.nan,2133,5433,np.nan,4432]},
 8columns =['id','date','city','category','age','price'])

#创建自定义函数
def table_info(x):
    shape=x.shape
    types=x.dtypes
    colums=x.columns
    print("数据维度(行，列):\n",shape)
    print("数据格式:\n",types)
    print("列名称:\n",colums)

#调用自定义函数获取 df 数据表信息并输出结果
table_info(df)

数据维度(行，列):
(6, 6)
数据格式:
id int64
date datetime64[ns]
city object
category object
age int64
price float64
dtype: object
列名称:
Index(['id', 'date', 'city', 'category', 'age', 'price'], dtype='object')

````









```python

```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/.jpg) 
![image](https://github.com/2804983329/data-analysis/blob/master/picture/.jpg) 
















