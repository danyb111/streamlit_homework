# %%

import streamlit as st
import pandas as pd

# %% Codigo para la pagina de Streamlit

st.write("""
# Visualizador de archivos CSV y JSON
Sube el archivo que quieres visualizar.
         """)

# %% Cargando archivo

file = st.file_uploader('Sube un archivo CSV o JSON', type = ['csv', 'json'])

if file is not None:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    if file.name.endswith('json'):
        df = pd.read_json(file)


    # Mostrar el DataFrame

    st.write('Contenido del archivo')
    st.dataframe(df)



# Correr esto en la terminal

# streamlit run streamlit_homework.py
