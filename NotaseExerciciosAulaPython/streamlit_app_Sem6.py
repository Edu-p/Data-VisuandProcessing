import pandas    as pd
import streamlit as st

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

if( ( f_zipcode!= [] ) & ( f_attributes != [] )):
    data = data.loc[ data['zipcode'].isin( f_zipcode ), f_attributes ] # apareer o que foi selecionado, so se ele selecionou

elif(  ( f_zipcode!= [] ) & ( f_attributes == [] ) ):
    data = data.loc[ data['zipcode'].isin(f_zipcode), : ]

elif(  ( f_zipcode== [] ) & ( f_attributes != [] ) ):
    data = data.loc[ :, f_attributes ]
else:
    data = data.copy()

# st.write( data.head(7) )

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

st.dataframe(df, height=600)

# st.write( df.head(7) )
