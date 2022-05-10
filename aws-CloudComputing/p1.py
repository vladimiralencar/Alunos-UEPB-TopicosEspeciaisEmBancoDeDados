import pandas as pd

url = 'https://raw.githubusercontent.com/vladimiralencar/Alunos-UEPB-TopicosEspeciaisEmBancoDeDados/master/Python-Para-Analise-de-Dados/Casos_por_cidades.csv'

df = pd.read_csv(url)
print(len(df))
print(df.head())
 

df2 = df.sort_values(by='last_available_confirmed', ascending=False)
df3 = df2[:15].reset_index(drop=True)
print(df3)

print('Ultimos casos confirmados')

print(df3.loc[:, ['city', 'last_available_confirmed']])

