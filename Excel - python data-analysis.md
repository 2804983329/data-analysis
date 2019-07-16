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



