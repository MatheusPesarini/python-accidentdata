import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo
dados = pd.read_excel("acidentes.xlsx")

# Criando uma figura com quatro subplots
fig, axs = plt.subplots(4, 1, figsize=(12,24))

# Para cada coluna
for i in range(4):
    # Selecionando a coluna
    coluna = dados.iloc[:, i]

    # Contando a frequência de cada valor
    frequencia = coluna.value_counts()

    # Se a coluna é a primeira ou a segunda
    if i < 2:
        # Filtrando os valores com frequência maior que 1000
        frequencia = frequencia[frequencia > 2000]

    # Plotando o gráfico
    sns.barplot(x=frequencia.index, y=frequencia.values, ax=axs[i])
    axs[i].set_title('Coluna ' + str(i+1))
    axs[i].set_xlabel('Valor')
    axs[i].set_ylabel('Frequência')
    plt.xticks(rotation=90)

# Ajustando o espaço no fundo do gráfico
plt.subplots_adjust(bottom=0.25)

plt.show()