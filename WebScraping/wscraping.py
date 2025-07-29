# Importação das bibliotecas necessárias
import pandas as pd                # Para manipulação de dados com DataFrame
import numpy as np                 # Para operações numéricas
import matplotlib.pyplot as plt    # Para visualização gráfica
import seaborn as sns              # Para visualização estatística com gráficos mais elegantes
# %matplotlib inline              # Comentado: Usado em notebooks Jupyter para mostrar gráficos dentro do notebook

# Importando bibliotecas para web scraping
from urllib.request import urlopen        # Para abrir a URL
from bs4 import BeautifulSoup             # Para fazer parsing do HTML

# Definição da URL que contém os resultados da corrida
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)                       # Abre e lê o conteúdo HTML da página

# Utiliza o BeautifulSoup para fazer o parsing do HTML com o parser 'lxml'
soup = BeautifulSoup(html, 'lxml')

# Exibe o tipo do objeto soup
type(soup)

#  obter o título da página
# title = soup.title
# print(title)

#  listar todos os links <a> da página
# all_links = soup.find_all("a")
# for link in all_links:
#     print(link.get("href"))

# Busca todas as linhas da tabela (tags <tr>)
rows = soup.find_all('tr')
print(f"Total de linhas (tr): {len(rows)}")  # Mostra a quantidade de linhas encontradas

# Busca todas as células da tabela (tags <td>)
row_td = soup.find_all('td')
print(f"Total de celulas (td): {len(row_td)}")  # Mostra a quantidade de células encontradas

# Converte todas as células para string
str_cells = str(row_td)
# Usa BeautifulSoup novamente para limpar as tags HTML e deixar só o texto
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
# print(cleantext)

# Importa a biblioteca de expressões regulares para limpeza
import re

# Inicializa uma lista vazia para armazenar os dados processados
list_rows = []

# Para cada linha da tabela...
for row in rows:
    cells = row.find_all('td')          # Encontra todas as células da linha
    str_cells = str(cells)              # Converte a lista de células para string
    clean = re.compile('<.*?>')         # Expressão regular para remover tags HTML
    clean2 = re.sub(clean, '', str_cells)  # Aplica a limpeza com regex
    list_rows.append(clean2)            # Adiciona a linha limpa na lista

# Cria um DataFrame a partir da lista de linhas
df = pd.DataFrame(list_rows)
print(df.head(10))  # Exibe as 10 primeiras linhas

# Divide o conteúdo da coluna 0 do DataFrame em várias colunas, usando vírgula como separador
df1 = df[0].str.split(',', expand=True)
print(df1.head(10))  # Exibe as 10 primeiras linhas do novo DataFrame

# Busca os rótulos das colunas (tags <th>)
col_labels = soup.find_all('th')

# Inicializa lista para armazenar os rótulos
all_header = []

# Converte os rótulos para string
col_str = str(col_labels)
# Remove as tags HTML e deixa apenas o texto
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
# Adiciona o texto limpo à lista
all_header.append(cleantext2)
print(all_header)  # Mostra os rótulos brutos

# Cria DataFrame com os rótulos (tudo ainda em uma única string)
df2 = pd.DataFrame(all_header)
df2.head()

# Divide a string dos rótulos em colunas separadas
df3 = df2[0].str.split(',', expand=True)
df3.head()

# Junta (concatena) os rótulos (df3) com os dados (df1)
frames = [df3, df1]
df4 = pd.concat(frames)  # Concatena verticalmente
df4.head(10)

# Renomeia as colunas do DataFrame com base na primeira linha (que são os rótulos)
df5 = df4.rename(columns=df4.iloc[0])
print(df5.head())  # Exibe o DataFrame final com colunas nomeadas

# Mostra as informações do DataFrame (tipo de dados, colunas, valores nulos, etc.)
df5.info()

# Mostra o formato (linhas, colunas) do DataFrame
df5.shape

df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])


df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Team]': 'Team'},inplace=True)
df7['Team'] = df7['Team'].str.strip(']')
print(df7.head())

