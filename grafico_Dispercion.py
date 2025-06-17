import pandas as pd
import plotly.express as px
import streamlit as st

def crear_grafico(df):
    df_mapa = df.sample(200, random_state=42)

    graf_mapa = px.scatter_geo(
        df_mapa,
        lat='Latitude',
        lon='Longitude',
        scope='usa',
        locationmode='USA-states',
        template='seaborn',
        color='Median_House_Value',  # 🎯 color según precio
        color_continuous_scale=['lightgreen', 'yellow', 'orange', 'red'], 
        hover_name='Median_House_Value',
        hover_data={'Latitude': False, 'Longitude': False},
        title='Precio segun su ubicación'
    )

    graf_mapa.update_geos(
        lataxis_range=[32, 42.5],
        lonaxis_range=[-125, -114],
        showland=True,
        fitbounds="locations"
    )

    graf_mapa.update_layout(
        coloraxis_colorbar=dict(
            title='Valor de Vivienda',
            ticksuffix='$',
            showticksuffix='last'
        )
    )

    return graf_mapa
