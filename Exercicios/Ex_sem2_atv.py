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

#print(dataAtv2[['price','dormitory_type']][dataAtv2['bedrooms'] == 1].head(30))

# Pergunta 3

dataAtv2['condition_type'] = 'standard'

dataAtv2.loc[dataAtv2['condition'] <= 2, 'condition_type'] = 'bad'
dataAtv2.loc[(dataAtv2['condition'] == 3) | (dataAtv2['condition'] == 4), 'condition_type'] = 'regular'
dataAtv2.loc[dataAtv2['condition'] == 5, 'condition_type'] = 'good'

#print(dataAtv2[['price','condition_type','condition']][dataAtv2['condition_type'] == 'bad'].head(30))

# Pergunta 4

dataAtv2['condition'] = dataAtv2['condition'].astype( str )

#print(dataAtv2.dtypes)

# Pergunta 5

cols = ['sqft_living15','sqft_lot15']

dataAtv2 = dataAtv2.drop(cols,axis=1)

#print(dataAtv2.columns)

# Pergunta 6

dataAtv2['yr_built'] = pd.to_datetime(dataAtv2['yr_built'])

#print(dataAtv2.dtypes)

# Pergunta 7

dataAtv2['yr_renovated'] = pd.to_datetime(dataAtv2['yr_renovated'])

#print(dataAtv2.dtypes)

# Pergunta 8

#print( dataAtv2[['yr_built']].sort_values('yr_built').max() )

# Pergunta 9

#print( dataAtv2[['yr_renovated']].sort_values('yr_renovated') )

# Pergunta 10

#print( dataAtv2[['floors']][dataAtv2['floors'] == 2].shape )

# Pergunta 11

#print( dataAtv2[['condition_type']][dataAtv2['condition_type'] == 'regular'].shape )

# Pergunta 12

#print(dataAtv2.columns)

#print( dataAtv2[['condition_type']][(dataAtv2['condition_type'] == 'bad') & (dataAtv2['view'] == 1)].shape )

# Pergunta 13

print( dataAtv2[['condition_type']][(dataAtv2['condition_type'] == 'good') & (dataAtv2['house_age'] == 'new_house')].shape )










