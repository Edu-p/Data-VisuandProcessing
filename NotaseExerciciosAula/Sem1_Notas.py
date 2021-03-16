
import pandas as pd

#ler o arquivo .csv

data = pd.read_csv('../datasets/kc_house_data.csv')

#mostre as linhas primeiras linhas do conj de dados

print( data.head() )

#mostre o numeor de colunas e linhas do conj de dados

print( data.shape )

#mostrar na tela o nome das colunas do conj de dados

print( data.columns )

#mostre na tela o conjunto de dados ordenados pela coluna price

print( data[['id','price']] .sort_values('price') )

#mostrar na tela o conj ordenado pela coluna price so que decrescente

print( data[['id','price']].sort_values('price',ascending=False) )
