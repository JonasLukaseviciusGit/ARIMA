# ARIMA
Bandymai pritaikyti ARIMA kriptovaliutų kainų prognozavimui

prices_close.csv - dataset'as

AIC.py - randa optimalius parametrus (d, p, q) ARIMA modeliui pagal AIC
adfuller.py - skaičiuoja dataset'o stacionarumą
fitting.py - fittin'a modelį
testing.py - testuoja sufittin'tą modelį
log+mean+standarddev.py - transformuoja kainas logaritmu, o tada skaičiuoja rolling mean ir standard deviation
train_test_visualization - vizualiai atvaizduoja train ir test segmentus grafike

Problema - testuojant modelius su skirtingais parametrais generuojamos identiškos arba labai mažai besiskiriančios ir kylančios vertės (prognozės)
