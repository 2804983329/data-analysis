import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#% matplotlib inline   #用在Jupyter notebook中具体作用是当你调用matplotlib.pyplot的绘图函数plot()进行绘图的时候，或者生成一个figure画布的时候

sns.set_style("darkgrid")
sns.set_context("paper")
#设置风格、尺度

import warnings
warnings.filterwarnings('ignore')
#不发出警告


#折线图

df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000',periods=1000), columns=list('ABCD'))
df = df.cumsum()
df.plot(kind='line',   #bar 柱状图  line折线图
        style = '--',
        alpha = 0.4,
        use_index = True, #是否使用坐标
        rot = 45,    #是否旋转
        grid = True, #是否格网图
        figsize = (8,4),  #图的大小
        title = 'test',
        legend = True,
        subplots = False,
        colormap = 'Greens')
#subplots → 是否将各个列绘制到不同图表，默认False
#也可以 → plt.plot(df)


#散点图 、 气泡图

plt.figure(figsize=(8,6))
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y,marker='.',
            s = np.random.randn(1000)*100,
            cmap = 'Reds',
            c = y,
            alpha=0.8)
#s:散点的大小
#c:散点的颜色
#vmin，vmax：亮度设置，标量
#cmap：colormap




