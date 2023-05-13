import pandas as pd
from statsmodels.tsa.arima.model import ARIMAResults
import matplotlib.pyplot as plt

path = r'C:\Users\HP\Documents\DS\datasets\BTC-USDT'
df = pd.read_csv(path)

print(df)

size = 1000                 # naudojamos dataset'o dalies dydis

df = df.tail(size)          # imamos paskutines 1000 eiluciu

size = df.shape
print(size)
rows = size[0]

split = int((-1 * rows) / 2)    # train - test atskyrimo indeksas

train = df.iloc[:split]
test = df.iloc[split:]

print('-----')

print(train.shape, test.shape)

model = ARIMAResults.load(r'C:\Users\HP\Documents\DS\baigiamasis\trained_models\ARIMA\(3, 1, 2)_10--4')

preds = model.predict(start=test.index[3], end=test.index[-1], dynamic=False)

predictions = [[pred, close] for pred, close in zip(preds, test['close'])]

for pred, actual in predictions:
    print(f"Prediction: {pred:.10f}, Actual: {actual:.2f}")

indices = range(len(preds))
plt.plot(indices, preds)
plt.show()