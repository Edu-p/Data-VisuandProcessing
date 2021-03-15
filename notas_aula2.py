import pandas as pd

dataF = pd.read_csv('datasets/kc_house_data.csv')

# mostrar tipos de variaveis de cada coluna
#print( dataF.dtypes )

# funçao que converte tipo object(string) -> date

dataF['data'] = pd.to_datetime(dataF['date'])

print(dataF['data'])

