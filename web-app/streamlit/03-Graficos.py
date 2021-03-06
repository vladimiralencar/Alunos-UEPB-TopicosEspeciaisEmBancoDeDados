import streamlit as st
import numpy as np
import pandas as pd

st.title('Gráfico app')

st.write("tabela (dataframe):")

data =  np.array( [
     [18, 19, 21, 40, 38, 50, 19, 20], # 'Idade'
     [55, 60, 63, 77, 73, 60, 57, 70]  ])# 'Peso'



df = pd.DataFrame(data.T, columns = ['Idade', 'Peso'])

#df = df.set_index(df.Idade)
#df.index = 'Idade'
#del df['Idade']

st.write(df)

#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

st.line_chart(df.Idade)
st.line_chart(df.Peso)

#st.bar_chart(df)

st.bar_chart(df.Idade)
st.bar_chart(df.Peso)

# No prompt de Comando Executar:
# streamlit run 03-Graficos.py