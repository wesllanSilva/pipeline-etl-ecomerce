import pandas as pd 
import sqlite3
from datetime import datetime

#definir caminho do arquivo JSONL
df = pd.read_json('../data/data.jsonl', lines=True)

#Setar o pandas para mostrar todas as colunas
pd.options.display.max_columns =None

#Adicionar a coluna_source com valor fixo
df['_source'] = "https://lista.mercadolivre.com.br/tenis-corrida-masculino"

#Adicionar coluna _data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

#Tratar os valores nulos para as colunas numéricas e de texto
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

#Remover os parênteses das colunas 'reviews_amount'
df['reviews_amount'] = df['reviews_amount'].str.replace('[\(\)]', '', regex=True)
df['reviews_amount'] = df['reviews_amount'].fillna(0).astype(int)

#Tratar os preços como floats e calcular totais
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

#Remover as colunas antigas
df.drop(columns =['old_price_reais','old_price_centavos','new_price_reais','new_price_centavos'])

#conectar ao banco de dados SQLite(ou criar novo)
conn = sqlite3.connect('../data/analisepreco.db')

#Salvar o dataframe no banco SQlite
df.to_sql('mercadolivre_itens', conn, if_exists='replace', index=False)

#Fechar conexão com o banco de dados
conn.close()


print(df.head())