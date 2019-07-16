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














