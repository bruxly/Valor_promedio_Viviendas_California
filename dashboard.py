from pdf2image.pdf2image import convert_from_path
import streamlit as st
import pandas as pd
import plotly.express as px
import grafico_mapa as graf1
import grafico_Dispercion as graf2
import precio_ingresos as graf3

from pdf2image import convert_from_bytes


st.set_page_config(layout='wide')#siempre va mostrar modo ancho de la pantalla 


#imagen
st.sidebar.title("Alumno: Rodrigo Patiño")
st.sidebar.image('logo.jpg')

# Barra lateral con menú de navegación

st.sidebar.title("Back-end")
opcion = st.sidebar.radio("Menú", ["Inicio", "README", "Gráficas","Certificado"])


if opcion == "Inicio":
    

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


elif opcion == "README":
    
    st.title("📄 README - Detalles del Proyecto")

    st.markdown("""
    ## 🏡 Proyecto de Predicción de Precios de Vivienda en California

    ---

    ### 📈 Problema de Negocio
    <p style="font-size:20px">
    Este proyecto tiene como objetivo predecir los precios de las viviendas en California utilizando datos geoespaciales y características de las propiedades.  
    Se explora el modelo de *machine learning* **XGBoost** para ayudar a comprender cómo varían los precios según la ubicación y las características de las viviendas.
    </p>
    ---

    ### ❓ Preguntas Clave
    <p style="font-size:20px">
    - 🔍 **Análisis Inicial**: ¿Qué *insights* podemos obtener del análisis exploratorio inicial del conjunto de datos?
    - 🛠️ **Transformaciones**: ¿Qué preprocesamiento es necesario para preparar los datos correctamente?
    - 🌍 **Influencia Geográfica**: ¿Cómo afecta la ubicación (latitud, longitud, distancia a la costa) a los precios de las viviendas?
    - 🏠 **Características de las Viviendas**: ¿Qué características como el número de habitaciones o el tamaño de las viviendas influyen más en los precios?
    </p>
    ---

    ### 🚀 Configuración del Ambiente
    <p style="font-size:20px">
    Asegúrate de tener las siguientes herramientas y bibliotecas instaladas:

    <p style="font-size:20px">
    - Google Colaboratory
    </p>
    <p style="font-size:20px">
    - Pandas
    </p>
    <p style="font-size:20px">
    - NumPy
    </p>
    <p style="font-size:20px">
    - Plotly
    </p>
    <p style="font-size:20px">
    - XGBoost
    </p>
    <p style="font-size:20px">
    - Scikit-learn
    </p>

    ---

    ### 📥 Obtención y Tratamiento de Datos
    <p style="font-size:20px">
    - **Cargando la Base de Datos**: 
    </p> 
    <p style="font-size:20px">
    Los datos provienen del conjunto de datos *California Housing*, disponible en formato `.csv`.
    </p> 
    ---

    ### 🧹 Tratamiento de Datos
    <p style="font-size:20px">
    Durante el preprocesamiento se realizan las siguientes operaciones:
    </p>
    <p style="font-size:20px">
    - 🧽 **Manejo de Valores Faltantes**:  
    </p>
    <p style="font-size:20px">           
    Se imputan o eliminan valores faltantes en las variables clave.
    </p> 
    <p style="font-size:20px">   
    - 🚫 **Eliminación de Duplicados**: 
    </p>  
    <p style="font-size:20px">   
    Se identifican y eliminan filas duplicadas en el conjunto de datos.
    </p>  
    <p style="font-size:20px">  
    - 📉 **Manejo de Outliers**:
    </p> 
    <p style="font-size:20px">   
    Se utilizan técnicas como el rango intercuartílico (IQR) para gestionar valores atípicos en el precio de las viviendas.
    </p>
    ---

    ### 📊 Normalización de Datos
    <p style="font-size:20px">
    Se eliminan columnas irrelevantes y se normalizan las variables para asegurar que los modelos tengan un rendimiento óptimo.
    </p>         
    ---
    <p style="font-size:20px">           
    Este proyecto tiene como objetivo predecir los precios de las viviendas en California utilizando datos geoespaciales y características de las propiedades. Se utilizo el modelo XGBoost para ayudar a comprender cómo varían los precios según la ubicación y las características de las viviendas
    </p>    

    """, unsafe_allow_html=True)



elif opcion == "Gráficas":
    st.title("📊 Galería de Gráficas desde PDF")

    # Ruta local al archivo PDF (debe estar en la misma carpeta del script o especificar la ruta)
    ruta_pdf = "graficas.pdf"

    try:
        paginas = convert_from_path(ruta_pdf)

        st.info("Mostrando las gráficas contenidas en el PDF…")

        for i, pagina in enumerate(paginas):
            st.image(pagina, caption=f"Gráfica {i+1}", use_container_width=True)

    except Exception as e:
        st.error(f"❌ Error al cargar el PDF: {e}")


elif opcion == 'Certificado':
    st.title('Certificado del Proyecto')
