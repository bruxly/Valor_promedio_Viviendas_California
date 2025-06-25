import streamlit as st
import pandas as pd
import plotly.express as px
import grafico_mapa as graf1
import grafico_Dispercion as graf2
import precio_ingresos as graf3

from PIL import Image



st.set_page_config(layout='wide')#siempre va mostrar modo ancho de la pantalla 


#imagen
st.sidebar.title("Alumno: Rodrigo Patiño")
st.sidebar.image('logo.jpg')

# Barra lateral con menú de navegación

st.sidebar.title("Back-end")
opcion = st.sidebar.radio("Menú", ["Inicio", "Certificado","Instructores","README", "Gráficas"])


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



elif opcion == 'Certificado':
    st.title('Certificado del Proyecto')
    st.image('certificado.png')





elif opcion == 'Instructores':
    st.markdown(
        "<h1 style='text-align: center; font-size: 3.5em;margin-bottom: 40px;'>Bootcamp Xperience</h1>", 
        unsafe_allow_html=True
    )
    col1, col2 = st.columns(2)

    imagen1 = Image.open('alejo.png')
    imagen2 = Image.open('sergio.png')

    altura_deseada = 300

    # Escalar manteniendo proporciones
    def escalar_altura(img, altura_objetivo, ampliar_ancho=False):
        ancho_original, alto_original = img.size
        factor = altura_objetivo / alto_original
        nuevo_ancho = int(ancho_original * factor)
        
        if ampliar_ancho:
            nuevo_ancho = int(nuevo_ancho * 1.15)  # Aumentar el ancho un 15%
        
        return img.resize((nuevo_ancho, altura_objetivo))

    imagen1_redimensionada = escalar_altura(imagen1, altura_deseada, ampliar_ancho=True)
    imagen2_redimensionada = escalar_altura(imagen2, altura_deseada)

    
    with col1:
        st.image(imagen1_redimensionada)

    with col2:
        st.image(imagen2_redimensionada)
    




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

    url_pdf = "https://raw.githubusercontent.com/bruxly/Valor_promedio_Viviendas_California/main/Graficas.pdf"

    try:
        st.markdown(
            f'<a href="{url_pdf}" target="_blank" rel="noopener noreferrer">📄 Abrir PDF en una nueva pestaña</a>',
            unsafe_allow_html=True
        )
        st.info("Haz clic en el enlace para ver las gráficas en el visor de tu navegador.")
    except Exception as e:
        st.error(f"❌ Error mostrando el PDF: {e}")


