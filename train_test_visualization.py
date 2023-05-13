import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams

path = r"C:\Users\HP\Documents\DS\datasets\BTC-USDT"
df = pd.read_csv(path)
df_close = df['close']

rcParams['figure.figsize'] = 10, 6
df_log = np.log(df_close)

train_data, test_data = df_log[3:int(len(df_log)*0.9)], df_log[int(len(df_log)*0.9):]
plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel('Dates')
plt.ylabel('Closing Prices')
plt.plot(df_log, 'green', label='Train data')
plt.plot(test_data, 'blue', label='Test data')
plt.legend()
plt.show()
