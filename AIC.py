import pandas as pd
from pmdarima import auto_arima

path = r"C:\Users\HP\Documents\DS\datasets\BTC-USDT"
df = pd.read_csv(path)
df = df.tail(10000)

stepwise_fit = auto_arima(df['close'], trace=True, suppress_warnings=True)
stepwise_fit.summary()