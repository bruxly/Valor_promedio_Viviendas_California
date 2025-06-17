import pandas as pd
import plotly.express as px
import streamlit as st
def crear_grafico(df):
    # Crear columna de relación ingreso/precio
    df['relacion_ingreso_precio'] = df['Median_House_Value'] / df['Median_Income']

    # Tomar muestra representativa
    df_muestra = df.sample(200, random_state=42)

    # Crear el mapa
    fig = px.scatter_geo(
        df_muestra,
        lat='Latitude',
        lon='Longitude',
        color='relacion_ingreso_precio',
        color_continuous_scale='bluered_r',
        title='Relación Ingreso / Precio de Vivienda en California',
        template='plotly_dark',
        
        hover_data={
            'Median_House_Value': True,
            'Median_Income': True,
            'Latitude': False,
            'Longitude': False,
            'relacion_ingreso_precio': ':.2f'
        },
        scope='usa',
        locationmode='USA-states'
    )

    fig.update_geos(
        lataxis_range=[32, 42.5],
        lonaxis_range=[-125, -114],
        showland=True,
        fitbounds="locations"
    )

    fig.update_layout(coloraxis_colorbar=dict(
        title="Relación<br>Precio / Ingreso",
        ticksuffix="x",
        tickformat=".1f"
    ))

    return fig