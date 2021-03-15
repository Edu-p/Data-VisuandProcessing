import pandas as pd
from numpy import int64

dataF = pd.read_csv('datasets/kc_house_data.csv')

# mostrar tipos de variaveis de cada coluna

print( dataF.dtypes )

# funçao que converte tipo object(string) -> date

dataF['data'] = pd.to_datetime(dataF['date'])



#----------------------
# Como converter TIPOS:
#----------------------

#Inteiro -> Float
dataF['bedrooms'] = dataF['bedrooms'].astype( float )

#Float -> Inteiro

'''
dataF['bedrooms'] = dataF['bedrooms'].astype( int )
print( dataF.dtypes )
 se fizer assim vai converter para int32 e tudo aqui ta sendo em int64,
 entao devemos especificar que é int64, que é uma informaçao que ve
 da biblicoteca numpy
 se nao fizermos isso nao da pra fazer operaçoes comuns com outras linhas 
 do conjunto de dados, ja que nesse caso esta tudo em int64
'''

dataF['bedrooms'] = dataF['bedrooms'].astype( int64 )

#Inteiro -> String

dataF['bedrooms'] = dataF['bedrooms'].astype( str )

#String -> Inteiro

dataF['bedrooms'] = dataF['bedrooms'].astype( int64 )

#String -> Date

dataF['data'] = pd.to_datetime(dataF['date'])

print( dataF.dtypes )

print( dataF[['id','bedrooms']].head(22) )


