import pandas as pd
import re
import csv

#################################

# string = "Geeks for 2"
pattern = re.compile("\\b[a-zA-Z]")  # first is letter
# if re.match(pattern, string):
#     print('ok')
# else:
#     print('not ok')

#################################

data = pd.read_csv('chamadas_ontem.csv')

# Form DataFrame from data
df = pd.DataFrame(
    data, columns=["Duração da chamada", "ID do chamador", "Destino"]
)

# number of maximum returned rows (default 60)
# pd.options.display.max_rows = 100
# print(pd.options.display.max_rows)

# Print the entire DataFrame
# print(df.to_string())

# Pandas will only return the first 5 rows, and the last 5 rows
# print(df)

# data_grp = data.groupby('ID do chamador')
# print(data_grp.first().to_string())


# for index, row in df.iterrows():

#     if re.match(pattern, row['ID do chamador']):
#         print(index, row['Duração da chamada'], row['ID do chamador'])
#     else:
#         continue


# Ligações Feitas
with open('chamadas_ontem_feitas.csv', 'w') as file:

    csv_writer = csv.writer(file)
    csv_writer.writerow(['Duração da chamada', 'ID do chamador'])

    for index, row in df.iterrows():

        if re.match(pattern, row['ID do chamador']):
            row = row['Duração da chamada'], row['ID do chamador']
            csv_writer.writerow(row)
        else:
            continue

# Ligações Recebidas
with open('chamadas_ontem_recebidas.csv', 'w') as file:

    csv_writer = csv.writer(file)
    csv_writer.writerow(['Duração da chamada', 'Destino'])

    for index, row in df.iterrows():

        if re.match(pattern, row['Destino']):
            row = row['Duração da chamada'], row['Destino']
            csv_writer.writerow(row)
        else:
            continue

# https://sparkbyexamples.com/pandas/pandas-groupby-count-examples/

##############################################################
# Ligações Feitas
dados = pd.read_csv('chamadas_ontem_feitas.csv')

# Form DataFrame from data
dataframe = pd.DataFrame(
    dados, columns=["ID do chamador"]
)

dados_grupo = dados.groupby(['ID do chamador'])[
    'ID do chamador'].count().reset_index(name='Chamadas feitas')
print(dados_grupo.to_string())


##############################################################
# Ligações Recebidas
dados = pd.read_csv('chamadas_ontem_recebidas.csv')

# Form DataFrame from data
dataframe = pd.DataFrame(
    dados, columns=["Destino"]
)

dados_grupo = dados.groupby(['Destino'])[
    'Destino'].count().reset_index(name='Chamadas recebidas')
print(dados_grupo.to_string())
