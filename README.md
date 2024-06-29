# pipeline-etl-ecomerce

# Objetivo do projeto é automatizar uma pesquisa de mercado de vários itens em sites de e-commerce

# Como Solução será Criado  um pipeline ETL para monitoramento dos produtos 

# Será utilizada algumas Bibliotecas Python:
 - Scrapy
 - Pandas
 - Streamlit

Coleta de dados com Scrapy 
- scrapy startproject coleta

Dentro da pasta Coleta 
- scrapy genspider mercadolivre https://lista.mercadolivre.com.br/tenis-corrida-masculino
    
    - o Spider tem 3 principais caracteristicas: Request - Parse - Next page

Para entrar dentro do terminal Scrapy
- scrapy shell

