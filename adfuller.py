import pandas as pd
from statsmodels.tsa.stattools import adfuller

path = r"C:\Users\HP\Documents\DS\datasets\BTC-USDT"
df = pd.read_csv(path)

def ad_test(dataset):
    dftest = adfuller(dataset, autolag='AIC')
    print('1. ADF : ', dftest[0])
    print('2. P-Value : ', dftest[1])
    print('3. Num Of Lags : ', dftest[2])
    print('4. Num Of Observations Used For ADF Regression and Critical Values Calculation : ', dftest[3])
    print('5. Critical Values :')
    for key, val in dftest[4].items():
        print('\t', key, ': ', val)

ad_test(df['close'])
