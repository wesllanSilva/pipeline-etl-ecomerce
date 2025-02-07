# pipeline-etl-ecomerce

# Objetivo do projeto é automatizar uma pesquisa de mercado de vários itens em sites de e-commerce

# Como Solução será Criado  um pipeline ETL para monitoramento dos produtos 

# Será utilizada algumas Bibliotecas Python:
 - Scrapy
 - Pandas
 - Streamlit

# Scrapy
Coleta de dados com Scrapy 
```bash
scrapy startproject coleta
```

Dentro da pasta Coleta 
```bash
scrapy genspider mercadolivre https://lista.mercadolivre.com.br/tenis-corrida-masculino
```
    - o Spider tem 3 principais caracteristicas: Request - Parse - Next page

Para entrar dentro do terminal Scrapy
```bash
scrapy shell
```
Adicionar seu AGENT_USER no arquivo settings do Scrapy:
AGENT_USER = ''

<h3>Request</h3>
fetch('https://lista.mercadolivre.com.br/tenis-corrida-masculino')

<h3>Parse</h3>

- response.css('div.ui-search-result__content')

Verificando quantos itens tem na pagina 
- len(response.css('div.ui-search-result__content')
)

Para percorrer toda a lista vamos utilizar o retorno yield dentro do laço de repetição

Para rodar o web scraping com retorno do arquivo em json:
```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```
 
- Para percorrer todas as paginas precisa alterar o settings para não obedecer a regra do ROBOTSTXT

Para rodar o pandas executar o arquivo main.py
```bash
python transformacao/main.py
```
# Streamlit
Para executar 
Instale as dependências necessárias:

```bash
pip install streamlit pandas sqlite3
```

Execute o aplicativo Streamlit:

```bash
streamlit run app.py
```

Acesse o aplicativo no navegador: Abra http://localhost:8501 no seu navegador para visualizar o aplicativo Streamlit.






