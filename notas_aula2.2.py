import pandas as pd
from numpy import int64

dataF = pd.read_csv('datasets/kc_house_data.csv')

#----------------------
# Criando novas variaveis:
#----------------------

# dataF['nomePica'] = "Eduzap"
# dataF['numero80'] = 80
# dataF['dataFormat'] = pd.to_datetime('2002-02-20')

# print(dataF[['id','date','nomePica','numero80','dataFormat']].head(3))
# print(dataF.dtypes)

#print(dataF.columns)

#----------------------
# deletando variaveis:
#----------------------

# .drop é a funçao que deleta do dataSet a coluna, tem que armazzenar
# o resultado em algum detaSet, pode ser ate o mesmo que vc dropou

# print(dataF.columns)
#
# dataF = dataF.drop('nomePica',axis=1) # esse axis=1 é deletar todas as linhas ao longo das colunas, depois explikcar direito isso
#
# print(dataF.columns)

# cols = ['nomePica','numero80','dataFormat'] # jeito de armazenar uma lista
#
# dataF = dataF.drop(cols,axis=1)# isso é uma lista, que a gente vai ver deposi, mas por agora é uma estrutura que guarda dados
#
# print(dataF.columns)

#----------------------
# Selecionando dados:
#----------------------

## Forma 1: Direto pelos nomes das colunas

print(dataF[['price','id','date']].head(2) )

## Forma 2: Pelos indices das linhas e colunas

#os dados sao dispostos da seguinte forma no pandas
# DADOS[linhas, colunas]
# o operador ':' se lê como ate, 0:3 de zero ate 3

#print(dataF[0:10,0:3]) isso aq da erro pq o pandas nao sabe o numero das colunas, temos que usar a funçao iloc

#print(dataF.iloc[0:2,0:3])

#dataF.iloc[:,:]=> selecioando todas as linhas e colunas do dataset

## Forma 3:Pelos indices das linhas e nome das colunas

print( dataF.loc[0:10,'price'] )
#aqui é loc pq agora estamos usando o nome da coluna para localizar o compilador entao usamos
#loc() so nao o iloc()


