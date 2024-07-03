import streamlit as st 
import pandas as pd 
import sqlite3 

#conectar ao BD
conn = sqlite3.connect('../data/analisepreco.db')

#carregar os dados da tabela em um DataFrame
pd.read_sql_query("SELECT * FROM mercadolivre_itens", conn)

#Fechar conexação