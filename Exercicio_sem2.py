import pandas as pd

dataF = pd.read_csv('datasets/kc_house_data.csv')

# 1. Qual a data do imovel mais antigo do portifolio

dataF['date'] = pd.to_datetime(dataF['date'])

print( dataF[['id','date','price']].sort_values('date',ascending=1).head(1) )

# 2. Quantos imoveis possuem o maximo de andares



# 3. Criar uma classificaçao para os imoveis, separando-os em alto e baixo padrao, se acordo om o preço(acima de 540.000 é alto padrao)
# 4. Relatorio ordenado pelo preço e contendo as seguintes informaçoes:
#     1. id do imovel
#     2. data que o imovel ficou disponivel para compra
#     3. numero de quartos
#     4. tamanho total do terreno
#     5. preço
#     6. classficacao do imovel(alto e baixo padrao)
#     7. Mapa indicando onde as casas tao localizadas geograficamente