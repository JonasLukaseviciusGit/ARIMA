import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

path = r"C:\Users\HP\Documents\DS\datasets\BTC-USDT"
df = pd.read_csv(path)
df_close = df['close']

rcParams['figure.figsize'] = 10, 6
df_log = np.log(df_close)
moving_avg = df_log.rolling(10000).mean()
std_dev = df_log.rolling(10000).std()
plt.legend(loc='best')
plt.title('Moving Average')
plt.plot(std_dev, color ="black", label = "Standard Deviation")
plt.plot(moving_avg, color="red", label = "Mean")
plt.legend()
plt.show()