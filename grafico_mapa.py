
import pandas as pd
import plotly.express as px


def crear_grafico(df):
    df_mapa = df.sample(200, random_state=42)
    graf_mapa = px.scatter_geo(df_mapa,
                           lat = 'Latitude',
                           lon = 'Longitude',
                           scope= 'usa',
                           locationmode = 'USA-states',
                           template = 'seaborn',
                           
                           hover_name='Median_House_Value',
                           hover_data = {'Latitude':False,'Longitude':False},
                           title = 'Precios de viviendas'
                           )

    graf_mapa.update_geos(
    lataxis_range=[32, 42.5],
    lonaxis_range=[-125, -114],
    showland=True,
    fitbounds="locations"
    )


    return graf_mapa