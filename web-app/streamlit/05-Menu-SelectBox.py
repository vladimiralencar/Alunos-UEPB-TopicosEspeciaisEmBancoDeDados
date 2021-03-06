import streamlit as st
import numpy as np
import pandas as pd

st.title('Menu app')

data =  np.array( [
     [18, 19, 21, 40, 38, 50, 19, 20], # 'Idade'
     [55, 60, 63, 77, 73, 60, 57, 70]  ])# 'Peso'



df = pd.DataFrame(data.T, columns = ['Idade', 'Peso'])

#df = df.set_index(df.Idade)
#df.index = 'Idade'
#del df['Idade']


option = st.selectbox(
    'Idade ?',
     df['Idade'])

'Idade Selecionada: ', option

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Pressione o Botão?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Dúvidas...")

# No prompt de Comando Executar:
# streamlit run 05-Menu-SelectBox.py
