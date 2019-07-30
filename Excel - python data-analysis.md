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


```python

```
![image](https://github.com/2804983329/data-analysis/blob/master/picture/.jpg) 
![image](https://github.com/2804983329/data-analysis/blob/master/picture/.jpg) 
![image](https://github.com/2804983329/data-analysis/blob/master/picture/.jpg) 





















