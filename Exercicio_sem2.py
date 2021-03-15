import pandas as pd

dataF = pd.read_csv('datasets/kc_house_data.csv')

# 1 Pergunta do CEO(qual a data do imovel mais antigo do portifolio)

#print( dataF[['id','date']].sort_values('date').min() )

# 2 Pergunta do CEO(quantos imoveis possuem o maximo de andares)

maxAndares = dataF.sort_values('floors').max()
#print( dataF[] )