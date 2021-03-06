import streamlit as st
import numpy as np
import pandas as pd

st.title('Dataframe app')

st.write("tabela (dataframe):")

data = {
    'Idade': [18, 19, 21, 40],
    'Peso': [55, 60, 63, 77]
}

df = pd.DataFrame(data)

st.write(df)

# No prompt de Comando Executar:
# streamlit run 02-Dataframe.py