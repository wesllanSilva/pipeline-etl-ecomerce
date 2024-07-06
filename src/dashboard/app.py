import streamlit as st 
import pandas as pd 
import sqlite3 

#conectar ao BD
conn = sqlite3.connect('../data/analisepreco.db')

#carregar os dados da tabela em um DataFrame
df = pd.read_sql_query("SELECT * FROM mercadolivre_itens", conn)

#Fechar conexação
conn.close()

#Titulo da Aplicação
st.title('Pesquisa de Mercado - Tênis no Mercado Livre')

#layout
st.subheader('KPIs principais')
col1,col2,col3 = st.columns(3)

#KPI 1: Número total de iitens
total_itens = df.shape[0]
col1.metric(label="Numero Total de Itens", value=total_itens)
#KPI 2: Número de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

#KPI 3: Preço Médio
average_price = df['price'].mean()
col3.metric(label="Preço Médio (R$)", value=f"{average_price:.2f}")

#Quais marcas são mais encontradas até a 10º página
st.subheader('Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_10_pages_brands = df.head(500)['brand'].value_counts().sort_values(ascending=False) 
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

#Qual o preços médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['price'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

#Qual a satisfação por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)

