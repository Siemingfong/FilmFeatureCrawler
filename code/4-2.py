import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
month=['Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr','May']
df = pd.DataFrame([[53, 0, 5, 3, 3],[51, 0, 1, 3, 2],[70, 4, 7, 5, 1],[66, 4, 1, 4, 2],[64, 4, 4, 3, 2],[69, 4, 7, 8, 2],[45, 2, 8, 4, 2],[29, 1, 6, 6, 1],[56, 4, 4, 2, 2],[41, 2, 2, 2, 1],[3, 0, 0, 0, 0],[8, 0, 0, 0, 0]],columns=['1000','2000','3000','4000','5000'],index=month)
plt.pcolor(df)
plt.colorbar()
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()


