import eurostat
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

r1= requests.get("https://api.idescat.cat/onomastica/v1/nadons/dades.json?id=40683&class=t&lang=en")

data = r1.text
data = json.loads(data)
ff = data['onomastica_nadons']['ff']['f']

num_marias = []
for dic in ff:
    maria = dic['pos1']['v']
    if dic['c'] in ['2017','2018','2019','2020','2021','2022']:
        num_marias.append(int(maria))
print(num_marias)
plt.bar(['2017','2018','2019','2020','2021','2022'],num_marias)
plt.xlabel('Años')
plt.ylabel('Marías')
plt.title('Número de mujeres que nacieron con nombre María en Cataluña en 2017-2022')
plt.show()
plt.savefig('ws2_marias.png')