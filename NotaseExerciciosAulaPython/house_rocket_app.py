import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.title( 'House Rocket Comp' )

st.markdown( 'Welcome to house rocket data analysis' )

st.header( 'Load data' )

# read data
@st.cache( allow_output_mutation=True )
def get_data( path ):
    data = pd.read_csv( path )
    data['date'] = pd.to_datetime( data['date'] )
    return data

# load data
data = get_data('../datasets/kc_house_data.csv')

# filter bedrooms

bedrooms = st.sidebar.multiselect(
    'Number of Bedrooms',
    data['bedrooms'].unique()
)

st.write('You choose', bedrooms[0])

# plot map
st.title( 'House Rocket Map' )
is_check = st.checkbox( 'Display map' )

# filters
price_min  = int(data['price'].min())
price_max  = int(data['price'].max())
price_avg  = int(data['price'].mean())

price_slider = st.slider( 'Price Range',
                          price_min,
                          price_max,
                          price_avg )

if is_check:
    # select rows
    houses = data[data['price'] < price_slider][['id', 'lat', 'long', 'price']]
    # st.dataframe( houses )

    # draw map
    fig = px.scatter_mapbox(houses,
                            lat='lat',
                            lon='long',
                            size='price',
                            color_continuous_scale=px.colors.cyclical.IceFire,
                            size_max=15,
                            zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    fig.show()