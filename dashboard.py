import streamlit as st
import pandas as pd
import plotly.express as px
import grafico_mapa as graf1
import grafico_Dispercion as graf2
import precio_ingresos as graf3

st.set_page_config(layout='wide')#siempre va mostrar modo ancho de la pantalla 

st.markdown(
    "<h1 style='text-align: center; margin-bottom: 40px;'>Valor Promedio de Viviendas en California 🏘️</h1>", 
    unsafe_allow_html=True
)



def formata_numero(valor, prefijo=''):
    for unidad in ['', 'k']:
        if valor < 1_000_000:
            return f'{prefijo} {valor:,.2f} {unidad}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        valor /= 1_000_000

    return f'{prefijo} {valor:,.1f} M'.replace(',', 'X').replace('.', ',').replace('X', '.')

#base de datos
df_ventas = pd.read_csv('https://raw.githubusercontent.com/bruxly/Valor_promedio_Viviendas_California/main/California_Houses.csv')

valor_maximo = df_ventas['Median_House_Value'].max()
valor_medio = df_ventas['Median_House_Value'].mean()
valor_minimo = df_ventas['Median_House_Value'].min()





#llamo a graficos
graf_mapa = graf1.crear_grafico(df_ventas)
graf_Dispercion =graf2.crear_grafico(df_ventas)
precio_ingresos =graf3.crear_grafico(df_ventas)


col1, col2, col3 = st.columns(3)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='text-align: center;'>Vivienda Premium</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: white;'>{formata_numero(valor_maximo)} $</h2>", unsafe_allow_html=True)
    st.plotly_chart(graf_mapa, use_container_width=True)

with col2:
    st.markdown("<h3 style='text-align: center;'>Vivienda media</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: white;'>{formata_numero(valor_medio)} $</h2>", unsafe_allow_html=True)
    st.plotly_chart(precio_ingresos, use_container_width=True)

with col3:
    st.markdown("<h3 style='text-align: center;'>Vivienda Básica</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: white;'>{formata_numero(valor_minimo)} $</h2>", unsafe_allow_html=True)
    st.plotly_chart(graf_Dispercion, use_container_width=True)


