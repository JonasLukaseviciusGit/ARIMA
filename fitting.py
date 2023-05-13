import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime
import matplotlib.pyplot as plt

path = r"C:\Users\HP\Documents\DS\datasets\BTC-USDT"
df = pd.read_csv(path)

size = 10000                    # imama 10 000 eiluciu
shift_back = 1000               # imami duomenys paslinkti per 1000 nuo galo,
                                # kad testing.py galetu imti nenaudotus duomenis - paskutinius 1000
df = df.tail(size)

df = df.set_index(pd.DatetimeIndex(df.index).to_period('T'))

print(df.shape)

start = int(-1 * (size + shift_back))
split = int(start + size / 2)           # test - train atskyrimo indeksas
end = int(-1 * shift_back)

train = df.iloc[start:split]
test = df.iloc[split:end]

print('-----')

print(train.shape, test.shape)

model = ARIMA(train['close'], order=(3, 1, 2), enforce_stationarity=False, enforce_invertibility=False)

print(datetime.now().strftime("%H:%M:%S"))

model = model.fit()

print(datetime.now().strftime("%H:%M:%S"))

summary = model.summary()
model.save(r'C:\Users\HP\Documents\DS\baigiamasis\trained_models\ARIMA\(3, 1, 2)_10--4')

print(summary)

indices = range(len(test['close']))
plt.plot(indices, test['close'])
plt.show()