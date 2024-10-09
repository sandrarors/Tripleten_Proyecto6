import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header("Análisis Vehículos en Venta")

hist_button = st.button('Construir Histograma') # crear un botón       
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches.')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir Diagrama de Dispersión') # crear un botón
if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un scatterplot para el conjunto de datos de anuncios de venta de coches.')

    # creas un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión 

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)