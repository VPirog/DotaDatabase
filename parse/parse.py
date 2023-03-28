import pandas as pd  # library for data analysis
import requests  # library to handle requests
from bs4 import BeautifulSoup  # library to parse HTML documents
import os


def parsing(wikiurl):
    table_class = "wikitable sortable"
    response = requests.get(wikiurl)
    # print(response.status_code)

    if(response.status_code == 200):
        print("Успешное подключение")

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': "wikitable"})

    df = pd.read_html(str(table))
    # convert list to dataframe
    df = pd.DataFrame(df[0])
    # print(df)
    os.mkdir(os.getcwd() + "/parse_out")
    with open('parse_out/out.csv', 'w'):
        df.to_csv('parse_out/out.csv')
    with open('parse_out/out.xlsx', 'w'):
        df.to_excel('parse_out/out.xlsx', sheet_name='Sheet_name_1')

    # # drop the unwanted columns
    # data = df.drop(["Rank", "Population(2001)"], axis=1)
    # # rename columns for ease
    # data = data.rename(columns={"City": "Neighborhood","State or union territory": "State","Population(2011)[3]": "Population"})
    # data.head()
