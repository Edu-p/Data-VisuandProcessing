import pandas as pd

dataF = pd.read_csv('datasets/kc_house_data.csv')

#1. Quantas casas estão disponíveis para compra?

print(dataF.shape[0])

#2. Quantos atributos as casas possuem?

print(dataF.shape[1])

#3. Quais são os atributos das casas?

print(dataF.columns)

#4. Qual a casa mais cara ( casa com o maior valor de venda )?

print(dataF[['id', 'price']].sort_values('price', ascending=False))

#5. Qual a casa com o maior número de quartos?

print(dataF[['id', 'bedrooms']].sort_values('bedrooms', ascending=False))

#6. Qual a soma total de quartos do conjunto de dados?

print(dataF['bedrooms'].sum())

#7. Quantas casas possuem 2 banheiros?

print(dataF[dataF['bathrooms'] == 2].shape)

#8. Qual o preço médio de todas as casas no conjunto de dados?

print(dataF['price'].mean())

#9. Qual o preço médio de casas com 2 banheiros?

print(dataF.loc[dataF['bathrooms'] == 2, 'price'].mean())

#10. Qual o preço mínimo entre as casas com 3 quartos?

print(dataF.loc[dataF['bedrooms'] == 3, 'price'].min())

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?

dataF['m2_living'] = dataF['sqft_living'] * 0.092
print(dataF[dataF['m2_living'] > 300].shape)

#12. Quantas casas tem mais de 2 andares?

print(dataF[dataF['floors'] > 2].shape)

#13. Quantas casas tem vista para o mar?

print(dataF[dataF['waterfront'] == 1].shape)

#14. Das casas com vista para o mar, quantas tem 3 quartos?

print(dataF[(dataF['waterfront'] == 1) & (dataF['bedrooms'] == 3)].shape)

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?

print(dataF[(dataF['m2_living'] > 300) & (dataF['bathrooms'] > 2)].shape)
