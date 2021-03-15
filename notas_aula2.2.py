import pandas as pd
from numpy import int64

dataF = pd.read_csv('datasets/kc_house_data.csv')

#----------------------
# Criando novas variaveis:
#----------------------

# dataF['nomePica'] = "Eduzap"
# dataF['numero80'] = 80
# dataF['dataFormat'] = pd.to_datetime('2002-02-20')
#
# print(dataF[['id','date','nomePica','numero80','dataFormat']].head(3))
# print(dataF.dtypes)

# print(dataF.columns)

#----------------------
# deletando variaveis:
#----------------------

