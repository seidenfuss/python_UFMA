import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_csv('/home/ananeves/Documents/Github/python_UFMA/projeto_final/presidente.csv',encoding='Latin 1', decimal=',', delimiter=';')
df.info()
candidatosQT=['Ciro Gomes','Lula','Padre Kelmon','Simone Tebet','Vera','Sofia Manzano','Bolsonaro', 'Eymael','Felipe Davila','Soraya','Leo Pericles']

votosQT=[]
for i in range(13,44,3):
  votosQT.append(df.iloc[8436,i])


# Ordena as categorias e valores em ordem decrescente dos valores
dados_ordenados = sorted(zip(votosQT, candidatosQT))
votosQT_ordenados, candidatosQT_ordenados = zip(*dados_ordenados)


plt.barh(candidatosQT_ordenados, votosQT_ordenados)
plt.ylabel("Candidatos")
plt.xlabel("Total de Votos (Milhões)")
plt.title("Primeiro Turno Eleições 2022 - Total de Votos")

# formatar notação do eixo para milhoes (1e6)
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: '{:.1f}'.format(x/1e6)))

plt.show()

candidatosPE=['Ciro Gomes','Lula','Padre Kelmon','Simone Tebet','Vera','Sofia Manzano','Bolsonaro', 'Eymael','Felipe Davila','Soraya','Leo Pericles','Branco','Nulo']

votos_PE=[]
for i in range(12,51,3):
  votos_PE.append((df.iloc[:,i].sum())/(df.iloc[8436,9]))

# Ordena as categorias e valores em ordem decrescente dos valores
dados_ordenados = sorted(zip(votos_PE, candidatosPE), reverse=True)
votosPE_ordenados, candidatosPE_ordenados = zip(*dados_ordenados)

plt.pie(votosPE_ordenados,  startangle=90,
        autopct=lambda pct: '{:.1f}%'.format(pct) if pct > 5 else '')
plt.legend(candidatosPE_ordenados, loc='right', bbox_to_anchor=(1.5, 0.5),title="Candidatos", fontsize=10)
plt.title("Eleições 2022 - 1º Turno")
plt.show()