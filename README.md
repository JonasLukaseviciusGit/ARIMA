# ARIMA
Bandymai pritaikyti ARIMA kriptovaliutų kainų prognozavimui

prices_close.csv - dataset'as

fitting.py - fittin'a modelį

testing.py - testuoja sufittin'tą modelį

AIC.py - randa optimalius parametrus (d, p, q) ARIMA modeliui pagal AIC

adfuller.py - skaičiuoja dataset'o stacionarumą

log+mean+standarddev.py - transformuoja kainas logaritmu, o tada skaičiuoja rolling mean ir standard deviation

train_test_visualization - vizualiai atvaizduoja train ir test segmentus grafike


Problema - testuojant modelius (testing.py) su skirtingais parametrais generuojamos identiškos arba labai mažai besiskiriančios ir kylančios vertės

Naudota literatūra ir pavyzdžiai:
https://www.sciencedirect.com/science/article/pii/S1877050922013382 - ARIMA lyginimas su LSTM akcijų kainoms prognozuoti
https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6
https://github.com/Ajaypal91/Predicting-Price-of-Cryptocurrency/blob/master/Models/ARIMA.py - ARIMA pavyzdys
https://github.com/jessgess/Time_Series_Analysis_ARIMA - ARMA su paaiškinimais pažingsniui
https://www.theaidream.com/post/stock-market-forecasting-using-time-series-analysis - kitas pavyzdys pažingsniui, naudojant ARIMA
