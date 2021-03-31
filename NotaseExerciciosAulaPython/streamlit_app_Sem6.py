import pandas    as pd
import streamlit as st
import numpy     as np
import folium

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config( layout='wide' ) # para que nossos elementos tenham a maxima largura possivel
@st.cache( allow_output_mutation=True ) #o '@' a gente chama de decorador e esse st.cache serve para nos lermos o arquivo direto da memoria e nao do disco,, no caso o dataset abaixo, o allow_.... é para que esse dataset possa mudar ao longo do codigo, isso agiliza a manipulaçao desse dataset

def get_data( path ):
    data = pd.read_csv( path )
    return data

# get data
path = '../datasets/kc_house_data.csv'
data = get_data( path )

# add new features
data['price_m2'] = data['price'] / (data['sqft_lot']/10.764)

#===============
# Data overview
#===============
f_attributes = st.sidebar.multiselect( 'Enter columns', data.columns )
f_zipcode = st.sidebar.multiselect( 'Enter zipcode',
                                    data['zipcode'].unique() )
st.title( 'Data Overview' )

# data filter
if( ( f_zipcode!= [] ) & ( f_attributes != [] )):
    data = data.loc[ data['zipcode'].isin( f_zipcode ), f_attributes ] # apareer o que foi selecionado, so se ele selecionou

elif(  ( f_zipcode!= [] ) & ( f_attributes == [] ) ):
    data = data.loc[ data['zipcode'].isin(f_zipcode), : ]

elif(  ( f_zipcode== [] ) & ( f_attributes != [] ) ):
    data = data.loc[ :, f_attributes ]
else:
    data = data.copy()

st.dataframe( data )

# st.write( data.head(7) )

c1, c2 = st.beta_columns( (1,1) ) # isso é para deixar os graficos dispostos um do lado do outro
# Avarage metrics

df1 = data[['id','zipcode']].groupby( 'zipcode' ).count().reset_index()
df2 = data[['price','zipcode']].groupby( 'zipcode' ).mean().reset_index()
df3 = data[['sqft_living','zipcode']].groupby( 'zipcode' ).mean().reset_index()
df4 = data[['price_m2','zipcode']].groupby( 'zipcode' ).mean().reset_index()

# merge metrics

m1 = pd.merge( df1,df2, on='zipcode', how='inner' )# abstrair inner por agora
m2 = pd.merge( m1,df3, on='zipcode', how='inner' )
df = pd.merge( m2,df4, on='zipcode', how='inner' )

df.columns = [ 'zipcode', 'total houses', 'price', 'sqft living', 'price/m2' ] # rename coluns

c1.header( 'Avarage values' )
c1.dataframe(df, height=600)

# st.write( df.head(7) )

# Descriptive Statistic
num_attributes = data.select_dtypes( include=['int64','float64'] )# selecionando todos as colunas que forem desses tipos
media   = pd.DataFrame( num_attributes.apply( np.nanmean ) )
mediana = pd.DataFrame( num_attributes.apply( np.median ) )
std     = pd.DataFrame( num_attributes.apply( np.nanstd ) )


max_    = pd.DataFrame( num_attributes.apply( np.max ) )
min_    = pd.DataFrame( num_attributes.apply( np.min ) )


df8 = pd.concat( [max_,min_,media,mediana,std], axis=1 ).reset_index()

df8.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

# st.write( num_attributes['price'].max() )

c2.header( 'Descriptive analysis' )
c2.dataframe(df8, height=600)


#===================
# Portfolio Density( MarkerCluster its a good type of map to show density )
#===================

st.title( 'Region Overview' )
c1, c2 = st.beta_columns( (1, 1) )

c1.header( 'Portfolio Density' )

df = data.sample( 15 ) # pegar uma amostra

# Base Map - Folium( map lib )
density_map = folium.Map( location=[data['lat'].mean(), data['long'].mean()] )

maker_cluster = MarkerCluster().add_to( density_map )
for name, row in df.iterrows(): # deixar meu dataframe interativo, row cada linha do dataset
    folium.Marker( [row['lat'], row['long'] ],
                   popup='Sold R$ on: {0}., {1} bedrooms'.format( row['price'],
                                                                 row['bedrooms'],
                                                                                     )
                   ).add_to( maker_cluster )


with c1:
    folium_static( density_map )


