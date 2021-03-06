import streamlit as st
import numpy as np
import pandas as pd

# Coordenadas de Campina Grande em graus decimais
latitude = -7.2305600
longitude = -35.8811100
    
st.title('Mapa app - Campina Grande e entornos')

area = 5

map_data = pd.DataFrame(
    np.random.randn(500, 2) / [area, area] + [latitude, longitude],
    columns=['lat', 'lon'])

st.map(map_data)


# No prompt de Comando Executar:
# streamlit run 04-mapa-App.py
