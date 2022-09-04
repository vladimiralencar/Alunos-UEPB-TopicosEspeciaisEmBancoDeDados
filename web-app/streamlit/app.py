# streamlit_app.py


#!pip install -q mysql-connector-python

# !pip install -q pymysql
# !pip install -q sqlalchemy

# streamlit rum app.py

import pandas as pd
import numpy as np

import streamlit as st
import mysql.connector
from mysql.connector import errorcode
user = 'root'
database = 'aulas'

c = st.container


st.title('Mysql Tools')

carregar_csv = st.sidebar.button("Carregar .csv")

consultar_tabela = st.sidebar.button("Consultar Tabela Mysql")

importar_tabela = st.sidebar.button("Importar Tabela para Mysql")

exportar_csv = st.sidebar.button("Exportar Tabela do Mysql para .csv")

st.text_input("Database:", key="database", value="aulas")
st.text_input("tabela:", key="tabela")
st.text_input("user:", key="user", value='root')
st.text_input("Password:", key="password", value='rootroot')

database = st.session_state.database
tabela = st.session_state.tabela
user = st.session_state.user
password = st.session_state.password
host = "127.0.0.1" # localhost
porta = 3600
schema = database

def conecta_banco_de_dados():
    import mysql.connector
    from sqlalchemy import create_engine
    erro = False
    try:
        conexao = "mysql+pymysql://" + user + ":" + password + "@" + host + '/' + schema
        # Abrir a Conexão
        engine = create_engine(conexao, echo = False, pool_recycle=porta)
        return conexao, engine
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            erro = "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            erro = "Database does not exist"
        else:
            erro = err
            st.write(erro)
        return False, False

def consulta_banco_de_dados(cnx, tabela):
        st.write('Tabela')
        query = "SELECT * from " + tabela +  " limit 100;"
        result_dataFrame = pd.read_sql(query,cnx)
        st.write('Tabela')
        st.write(result_dataFrame)

# principal

if carregar_csv:
    conexao, engine = conecta_banco_de_dados()
    if conexao != False: 
        consulta_banco_de_dados(conexao, tabela)
        conexao.close()

if consultar_tabela:
    conexao, engine  = conecta_banco_de_dados()
    if conexao != False: 
        consulta_banco_de_dados(conexao, tabela)
        conexao.close()


import chardet

st.write("Importar Tabela para Mysql")


# uploaded_file = st.file_uploader("Escolha um arquivo (*.csv)")
uploaded_file = None
file = None 

uploaded_file = st.file_uploader("Escolha um arquivo (*.csv)", key="upload_file")
file = st.session_state.upload_file
# if importar_tabela:
#     uploaded_file = st.file_uploader("Escolha um arquivo (*.csv)", key="upload_file")
#     file = st.session_state.upload_file

conexao, engine = False, False
if file is not None:
    df = pd.read_csv(file, encoding='latin-1') #, encoding='latin-1') #, encoding=result['encoding'])
    st.write(df)
    st.write("Importar Tabela para o  Mysql")
    conexao, engine = conecta_banco_de_dados()

    if conexao != False: 
        st.write('conectou')

        # importacao


        # host = "127.0.0.1" # localhost
        # porta = 3600
        # schema = database
        # conexao = "mysql+pymysql://" + user + ":" + password + "@" + host + '/' + schema

        # # Abrir a Conexão
        # engine = create_engine(conexao, echo = False, pool_recycle=porta)

        # dataframe => como tabela no MySQL
        df.to_sql(name = tabela, con = engine, if_exists = 'append', index = False)
        st.write('importado.')
        st.write(df)
        conexao.close()


        # df = pd.read_csv(uploaded_file, encoding='latin-1') #, encoding='latin-1') #, encoding=result['encoding'])

        # st.dataframe(df) 
        # print(df)
        # else:
        #     st.write('erro de conexao')
    # else:
    #     st.write('erro de upload')

        # with open(uploaded_file, 'rb') as f:
        #     result = chardet.detect(f.read())  # or readline if the file is large



        # # importacao
        # import mysql.connector
        # from sqlalchemy import create_engine

        # host = "127.0.0.1" # localhost
        # porta = 3600
        # schema = database
        # conexao = "mysql+pymysql://" + user + ":" + password + "@" + host + '/' + schema

        # # Abrir a Conexão
        # engine = create_engine(conexao, echo = False, pool_recycle=porta)

        # # dataframe => como tabela no MySQL
        # df.to_sql(name = tabela, con = engine, if_exists = 'append', index = False)
        # st.write('importado...')
        # st.write(df)
        # cnx.close()
    # else:
    #     st.write('ERRO')


#cnx.close()

# conn = init_connection()




# mydb = mysql.connector.connect(host="localhost", database = 'aulas',
#                         user="root", passwd="rootroot",use_pure=True)
# query = "SELECT * from brasil_cities limit 15;"
# result_dataFrame = pd.read_sql(query,mydb)

# st.write('<h1> Tabela </h1>')

# st.write(result_dataFrame)



# Mapa
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# rows = run_query("")
# fields = run_query("describe brasil_cities;")
# Print results.

# df = pd.DataFrame(rows)

# st.dataframe(df)

# for row in fields:
#     st.write(f"{row[0]} has a :{row[1]}:")

# for row in rows:
#     st.write(f"{row[0]} has a :{row[1]}:")