import eurostat
import pandas as pd
import matplotlib.pyplot as plt

# Construye el nombre del dataset
dataset_code = 'ei_bsco_m'

# Obtiene los datos
data = eurostat.get_data_df(dataset_code)

# Filtra los datos según los criterios
df = data.query('unit == "BAL" & indic == "BS-CSMCI" & s_adj == "SA"')

# Definir el rango de fechas que quieres (últimos 5 años en este caso)
start_year = 2022 - 5
end_year = 2022
columns_to_select = [f"{year}-{month:02}" for year in range(start_year, end_year + 1) for month in range(1, 13)]

# Selecciona solo las columnas del rango de fechas deseado
df1 = df[columns_to_select]

df1 = df1[12:13]
# Transponer el DataFrame
df1 = df1.T

# Agrupar por año y calcular la media
df1 = df1.groupby(df1.index.str.split('-').str[0]).mean()

plt.bar(['2017','2018','2019','2020','2021','2022'], list(df1.iloc[:, 0]))
plt.xlabel('Años')
plt.ylabel('Valor')
plt.title('EU Confidence 2017-2022')
plt.gca().invert_yaxis()

# Mostrar el gráfico
plt.show()
plt.savefig('eu_confidence_5years.png')


columns_to_select = [f"{2022}-{month:02}" for month in range(1, 13)]
df2 = df[columns_to_select]
df2 = df2[12:13]

plt.bar(['Jan','Feb','Mar','Apr','May','Jun,','Jul', 'Aug','Sep','Oct','Nov','Dec'], list(df2.iloc[0]))
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('EU Confidence 2017-2022')
plt.gca().invert_yaxis()
plt.show()
plt.savefig('eu_confidence_2022.png')




