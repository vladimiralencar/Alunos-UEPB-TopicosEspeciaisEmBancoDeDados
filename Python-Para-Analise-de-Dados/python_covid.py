import pandas as pd

url = 'https://raw.githubusercontent.com/vladimiralencar/Alunos-UEPB-TopicosEspeciaisEmBancoDeDados/master/Python-Para-Analise-de-Dados/Casos_por_cidades.csv'
df = pd.read_csv(url)

df2 = df.sort_values(by='last_available_confirmed', ascending=False)[:10]
at = [ 'city', 'last_available_confirmed' ]
print(df2[ at ][:5])


