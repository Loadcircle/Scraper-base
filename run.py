from bs4 import BeautifulSoup
import requests
import pandas
from pandas import DataFrame

url = 'https://www.e-inmob.com/agentes-inmobiliarios-en-mexico'

content = requests.get(url).content

resolve_content = BeautifulSoup(content, 'lxml')

div = resolve_content.findAll('div', {'class': 'team-members'})

obj = []

for el in div:
    name = el.find('h5').text
    tlf = el.findAll('p')[0].text
    email = el.findAll('p')[1].text

    obj.append({
        'Nombre': name,
        'Telefono': tlf,
        'Email': email
    })    

df = DataFrame(obj, columns=['Nombre', 'Telefono', 'Email'])

print(df)

try:
    export_csv = df.to_csv (r'C:\Users\jesus\Downloads\file.csv', index = None, header=True, encoding='utf_32') #Don't forget to add '.csv' at the end of the path
    print('Archivo exportado')

except Exception as e: 
    print(e)

print('------------------------End-------------------')
