import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

sns.set_style("darkgrid")
sns.set_context("paper")
#设置风格、尺度

import warnings
warnings.filterwarnings('ignore')
#不发出警告


#折线图

df = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000',periods=1000), columns=list('ABCD'))
df = df.cumsum()
df.plot(kind='line',
        style = '--',
        alpha = 0.4,
        use_index = True,
        rot = 45,
        grid = True,
        figsize = (8,4),
        title = 'test',
        legend = True,
        subplots = False,
        colormap = 'Green'
        )
#subplots → 是否将各个列绘制到不同图表，默认False
#也可以 → plt.plot(df)





