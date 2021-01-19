# carregue o conjunto  de dados do csv que baixamos  para o HD


#funçao- read_csv()
#biblioteca - pandas(utilizada muito para manipulaçao de dados)

from pandas import read_csv

#esse as é o apelido que vamos dar para a biblioteca pandas

iowa_file_path = 'kc_house_data.csv'

data = read_csv(iowa_file_path)