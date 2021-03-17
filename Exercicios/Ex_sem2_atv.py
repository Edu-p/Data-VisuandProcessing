import pandas as pd
import datetime as date

dataAtv2 = pd.read_csv('../datasets/kc_house_data.csv')

# Pergunta 1:

dataAtv2['date'] = pd.to_datetime(dataAtv2['date'])

dataAtv2['house_age'] = 'date'

diaD = pd.Timestamp("2015-01-01")

dataAtv2.loc[dataAtv2['date'] >= diaD, 'house_age'] = 'new_house'
dataAtv2.loc[dataAtv2['date'] < diaD, 'house_age'] = 'old_house'

#print(dataAtv2[['date','house_age']].head(40))

# Pergunta 2

dataAtv2['dormitory_type'] = 'standard'

dataAtv2.loc[dataAtv2['bedrooms'] == 1, 'dormitory_type'] = 'studio'
dataAtv2.loc[dataAtv2['bedrooms'] == 2, 'dormitory_type'] = 'apartament'
dataAtv2.loc[dataAtv2['bedrooms'] > 2, 'dormitory_type'] = 'house'

#print(dataAtv2[['price','dormitory_type']].head(30))
