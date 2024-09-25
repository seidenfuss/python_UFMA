#Questão 1: A cidade de São Joaquim encontra-se localizada no estado de Santa Catarina. Tendo em  vista sua latitude (28° 17’ 38”) e altitude (1.354 m), a citada cidade é considerada uma das mais  frias do Brasil. Ocasionalmente, nos dias de frio mais intenso, ocorrem precipitações sob a forma de  neve, sendo os meses mais frios julho e agosto. Dados obtidos no portal do Inmet  (https://portal.inmet.gov.br/dadoshistoricos, acesso em 12/07/2024) para o ano de 2023 apresentam  os valores de temperatura durante as 24 horas do dia e para todo o ano. Utilize as bibliotecas Panda,  Numpy e MatPlotlib para responder as seguintes questões (3 Pontos):

# Importar Bibliotecas: Panda, Numpy e MatPlotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ler arquivo "Sao_Joaquim.csv"
df = pd.read_csv('/home/ananeves/Documents/Github/python_UFMA/projeto_final/SaoJoaquim.CSV', encoding='iso-8859-1',\
                 decimal=',', delimiter=';', skiprows=8)

# acessar coluna H e remover NaN
temp=df['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'].dropna()

# calcular média
mediaT=np.mean(temp)
print(mediaT)

# calcular mínima
minT = np.min(temp)
print(minT)

# calcular máxima 
maxT = np.max(temp)
print(maxT)

# calcular desvio padrão
desvioT=np.std(temp)
print(desvioT)

# 2 – Faça o gráfico boxplot da temperatura na cidade de São Joaquim no ano de 2023. 
# Calcular quartis
q1 = np.quantile(temp, 0.25)
q2 = np.quantile(temp, 0.5)  # mediana
q3 = np.quantile(temp, 0.75)

# Calcular IQR
iqr = q3 - q1

# Calcular limites inferiores e superiores para outliers
upper_bound = q3 + 1.5 * iqr
print(upper_bound)
lower_bound = q1 - 1.5 * iqr
print(lower_bound)

# Criar boxplot
plt.boxplot(temp)
plt.xlabel('São Joaquim - SC - 2023')
plt.ylabel('TEMPERATURA DO AR - BULBO SECO (°C)')

# Add linhas para quartis e limites
plt.axhline(y=q1, color='r', linestyle='--', label='Quarti 1')
plt.axhline(y=q2, color='g', linestyle='--', label='Mediana (Q2)')
plt.axhline(y=q3, color='b', linestyle='--', label='Quartil 3')
plt.axhline(y=upper_bound, color='m', linestyle='--', label='Limite Superior')
plt.axhline(y=lower_bound, color='c', linestyle='--', label='Limite Inferior')

plt.legend()
plt.show()

# 3 – Faça um gráfico de barras com as temperaturas mínimas e máximas para cada mês do ano de  2023.

# Acertar o formato datetime 
df['Data'] = pd.to_datetime(df['Data'], format='%Y/%m/%d')

# Criar uma coluna com os meses
df['mes']=df['Data'].dt.month

# Agrupar e calcular média por mês
minT_mes = df.groupby('mes')['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'].min()
maxT_mes = df.groupby('mes')['TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)'].max()

print(minT_mes)
print(maxT_mes)

# Gráfico de Barras
meses = np.arange(1, 13)

largura = 0.3
plt.bar(meses - largura/2, minT_mes, width=largura, label='Temperatura Min')
plt.bar(meses + largura/2, maxT_mes, width=largura, label='Temperatura Max')

plt.xlabel('Meses')
plt.ylabel('Temperatura')
plt.title('Temperaturas Mensais')
plt.legend()
plt.show()