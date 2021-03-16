import pandas as pd

dataF = pd.read_csv('datasets/kc_house_data.csv')

# 1. Qual a data do imovel mais antigo do portifolio

dataF['date'] = pd.to_datetime(dataF['date'])

#print( dataF[['id','date','price']].sort_values('date',ascending=1).head(1) )




# 2. Quantos imoveis possuem o maximo de andares

#print(dataF['floors'].unique()) # o .unique pega todos os diferentes valores naquela coluna e os lista

#print( dataF[['id','price','floors']][dataF['floors'] == 3.5].shape )




# 3. Criar uma classificaçao para os imoveis, separando-os em alto e baixo padrao, se acordo om o preço(acima de 540.000 é alto padrao)

# dataF['level'] = 'standard'
#
dataF.loc[dataF['price'] > 540000,'level'] = 'high_level' # usando loc pq estou dando o nome especifico de uma coluna
dataF.loc[dataF['price'] <= 540000,'level'] = 'low_level'
#
# print(dataF[['id','price','level']].head(10))


# 4. Relatorio ordenado pelo preço e contendo as seguintes informaçoes:
#     1. id do imovel
#     2. data que o imovel ficou disponivel para compra
#     3. numero de quartos
#     4. tamanho total do terreno
#     5. preço
#     6. classficacao do imovel(alto e baixo padrao)

report_to_CEO = dataF[['id','date','bedrooms','sqft_lot','price','level']].sort_values('price',ascending=False)

report_to_CEO.to_csv( 'datasets/report_aula2.csv', index=False ) # o index false é para quando salvar no csv ele resetar os indices que mexemos na ordenaçao do ascending acima

#     7. Mapa indicando onde as casas tao localizadas geograficamente