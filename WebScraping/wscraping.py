import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
type(soup)
# Get the title
#title = soup.title
# print(title)

#LINKS
#all_links = soup.find_all("a")
#for link in all_links:
#    print(link.get("href"))

# Print the first 10 rows for sanity check
rows = soup.find_all('tr')
#print(rows[:10])

#for row in rows:
row_td = soup.find_all('td')
#print(row_td)
#type(row_td)

str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
#print(cleantext)

import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
#print(clean2)
#type(clean2)


df = pd.DataFrame(list_rows)
df.head(10)
df1 = df[0].str.split(',', expand=True)
df1.head(10)
