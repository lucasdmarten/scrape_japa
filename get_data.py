import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def get_data():

    paths = [
    "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/GO", 
    "https://www.resultadofacil.com.br/resultado-do-jogo-do-bicho/RJ"
    ]

    data={}
    dfs=[]
    for path in paths:
        request = requests.get(path)
        print(request.url)
        soup = BeautifulSoup(request.content, 'html.parser')
        tables = soup.find_all('tbody')
        titles = soup.find_all('h3', {"class":"g"})
        ntables = len(tables)
        for i in range(ntables):
            row = [table_text.text for table_text in tables[i].find_all('td')]
            length = len(row)
            name = soup.find_all('h3', {"class":"g"})[i].text[23:]
            if length == 28:
                n=0
                print(28)
                l=[]
                while n <= 28:

                    l.append(row[n:n+4]  + [titles[i].text[50:-40]])
                    n+=4
                dfs.append(pd.DataFrame(l)) 

            elif length == 40:
                n=0
                print(40)
                l = []
                while n <= 40:

                    l.append(row[n:n+4]  + [titles[i].text[50:-40]])

                    n+=4
                dfs.append(pd.DataFrame(l))

    for df in dfs:
        name=df.iloc[:,-1][0]
        df.to_csv('./data/{}.csv'.format(name))
    return dfs