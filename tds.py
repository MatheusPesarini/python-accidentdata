import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo
dados = pd.read_excel("acidentes.xlsx")

# Dividindo a primeira coluna em um novo dataframe
novos_dados = dados.iloc[:, 0].str.split(';', expand=True)

# Renomeando as colunas do novo dataframe
novos_dados.columns = ['causa', 'data', 'coluna3', 'coluna4', 'coluna5', 'coluna6']

# Convertendo a coluna de datas para datetime
novos_dados['data'] = pd.to_datetime(novos_dados['data'], errors='coerce')

# Concatenando o novo dataframe com o dataframe original
dados = pd.concat([novos_dados, dados.iloc[:, 1:]], axis=1)

# Filtrando os dados do mês de outubro
dados_outubro = dados[dados['data'].dt.month == 10]

# Acessando a coluna de causas
causas = dados_outubro['causa']

# Contando a frequência de cada causa
frequencia_causas = causas.value_counts()

# Filtrando as causas que ocorrem mais de 1000 vezes
frequencia_causas_filtrada = frequencia_causas[frequencia_causas > 1000]

# Plotando o gráfico
fig, ax = plt.subplots(figsize=(12,6))

sns.barplot(x=frequencia_causas_filtrada.index, y=frequencia_causas_filtrada.values, ax=ax)
ax.set_title('Causas de Acidentes Mais Ocorridas em Outubro')
ax.set_xlabel('Causa')
ax.set_ylabel('Frequência')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

plt.show()