import eurostat
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import numpy as np


file = pd.read_csv('newborns_catalonia.csv', sep=';')
girls = file['Girls']
girls_5years = girls[0:5]

r1= requests.get("https://api.idescat.cat/onomastica/v1/nadons/dades.json?id=40683&class=t&lang=en")

data = r1.text
data = json.loads(data)     
ff = data['onomastica_nadons']['ff']['f']

num_marias = []
for dic in ff:
    maria = dic['pos1']['v']
    if dic['c'] in ['2018','2019','2020','2021','2022']:
        num_marias.append(int(maria))


categories = ['2018','2019','2020','2021','2022']

fig, ax = plt.subplots()
width = 0.35  # Width of each bar
x = np.arange(len(categories))  # X-axis positions
print(list(girls_5years))
print(num_marias)
bar1 = ax.bar(x - width/2, list(girls_5years), width, label='Number of girls born per year')
bar2 = ax.bar(x + width/2, num_marias, width, label='Number of Marias born per year')

# Add labels and title
ax.set_xlabel('Years')
ax.set_title('Total women and women named Maria for the last 5 years')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.savefig('joined_barplot_girls_marias.png')
plt.show()




plt.bar(['2018','2019','2020','2021','2022'],num_marias)
plt.xlabel('Years')
plt.ylabel('Maria\'s')
plt.title('Women born in 2017-2022 named Maria')
plt.savefig('ws2_marias.png')
plt.show()

