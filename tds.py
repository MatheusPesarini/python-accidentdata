import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo
dados = pd.read_excel("acidentes.xlsx")

# Separando as informações por ';'
dados = dados.iloc[:, 0].str.split(';', expand=True)

# Selecionando a primeira coluna
acidentes = dados.iloc[:, 0]

# Contando a frequência de cada tipo de acidente
frequencia_acidentes = acidentes.value_counts()

# Filtrando os acidentes com frequência maior que 1000
frequencia_acidentes_filtrada = frequencia_acidentes[frequencia_acidentes > 1000]

# Plotando o gráfico
fig = plt.figure(figsize=(12,6))
sns.barplot(x=frequencia_acidentes_filtrada.index, y=frequencia_acidentes_filtrada.values)
plt.title('Acidentes Mais Ocorridos')
plt.xlabel('Tipo de Acidente')
plt.ylabel('Frequência')
plt.xticks(rotation=90)

# Ajustando o espaço no fundo do gráfico
plt.subplots_adjust(bottom=0.25)

plt.show()