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
![image](https://github.com/2804983329/data-analysis/blob/master/picture/chakanqiansanhangshuju.jpg)

### 查看后数据    
tail函数和head函数相反，用来查看数据表中后N行的数据，   
可以自己设置参数值来确定查看的行数。查询后三行示例如下：    
```
#查看最后三行
df.tail(``3``)
```

![image]()

## 03数据表清洗
第三部分是对数据表中的的问题进行清洗。主要内容包括对空值，大小写问题，数据格式和重复值的处理。   
不包含对数据间的逻辑验证。   

### 处理空值（删除或填充）   
我们在创建数据表的时候在price字段中故意设置几个NA值。对于空值的处理方式
有很多种，可以直接删除包含空值的数据，也可以对空值进行填充，比如用0填充或者用
均值填充。还可以根据不同字段的逻辑对空值进行推算。

excel 中可以通过“查找和替换” 功能对空值进行处理，将空值统一替换为0或均值
。也可以通过定位空值来实现。
![image](https://github.com/2804983329/data-analysis/blob/master/chulikongzhi1.jpg)


Python中处理空值的方法比较灵活，可以使用Dropna函数用来删除数据表中包含空值的数据
，也可以使用fillna函数对空值进行填充。下面代码和结构中可以看到使用dropna函数后，
包含NA值的两个字段已经不见了。返回的是一个不包含空值的数据表。
```
#删除数据表中含有空值的行
df.dropna(how='any')
```

![image](https://github.com/2804983329/data-analysis/blob/master/chulikongzhi2.jpg)


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
![image](https://github.com/2804983329/data-analysis/blob/master/chulikongzhi3.jpg)

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

![image](https://github.com/2804983329/data-analysis/blob/master/daxiaoxiezhuanhuan1.jpg)   


### 更改数据格式   
Excel中通过“设置单元格格式”功能可以修改数据格式，python中通过astype函数来修改数据格式

![image](https://github.com/2804983329/data-analysis/blob/master/genggaishujugeshi1.jpg)   

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
![image](https://github.com/2804983329/data-analysis/blob/master/genggailiemingcheng1.jpg) 

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































































































