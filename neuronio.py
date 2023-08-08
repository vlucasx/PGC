import math
import random
import pandas as pd
import matplotlib.pyplot as plt

# entradas = [4,0.5,1.1] # vetor de entrada 
# pesos = [0.1,0.3,0.4] # vetor de pesos
deslocamento = 1 # deslocamento inicial +1 para direita para que f(x>1) = 1
temperatura = 0.001  # 0.0001 forma um degrau razoável

def verificaEntradasEpesos(entradas, pesos): # verifica se a quantidade de entradas e de pesos é igual
  if len(entradas) > len(pesos):
    print("vetor de entradas maior que o de pesos")
    exit()
  elif len(entradas) < len(pesos):
    print("vetor de entradas menor que o de pesos")
    exit()


def funcaoAtivacao(net, deslocamento, temperatura):
  return 1/(1+(math.e)**(-((net-deslocamento)/temperatura)))


def calculaNet(entradas, pesos): # calcula o valor de rede (net):
  net = 0
  i=0

  for entrada in entradas:
    net = net + entrada * pesos[i]
    i=i+1

  return net

  
def neuronio(entradas, pesos, deslocamento, temperatura): # método do neurônio
  net = calculaNet(entradas, pesos)
  
  if funcaoAtivacao(net,deslocamento,temperatura) >= 1 : # Se f(x)>=1, o neurônio ativa sua saída. Se f(x) < 1, não ativa a saída.
      print("ativou: f("+str(net)+") = "+str(funcaoAtivacao(net,deslocamento,temperatura)))
      return False
  else:
    print("não ativou: f("+str(net)+") = "+str(funcaoAtivacao(net,deslocamento,temperatura)))
    return True


def criaFrutas(quantidade): # cria uma quantidade estipulada de "frutas"
  dados = []

  for i in range(quantidade):
    cor = random.uniform(0, 10)
    formato = random.uniform(0, 10)
    dados.append((cor, formato, "N/A"))
  
  return dados



def verificaMacas4var(dados, a,b, c,d): # verifica quais frutas são maçãs de acordo com as cacterísticas estipuladas nos intervalos a,b c,d que podem variar de 0 a 10.

  df = pd.DataFrame(dados, columns=['cor','formato', 'maçã?'])
  m=0
  
  for i in range(len(dados)):
    if a <= dados[i][0] <= b:
      if c <= dados[i][1] <= d:
        df.iloc[i, 2] = "sim"
        m = m+1    

  print("número de maçãs:", m)
  plotar(df)
  return df

def verificaMacas2var(dados, a,b): # verifica quais frutas são maçãs de acordo com as cacterísticas estipuladas no intervalo [a,b] que pode variar de 0 a 10.

  df = pd.DataFrame(dados, columns=['cor', 'formato', 'maçã?'])
  m=0
  
  for i in range(len(dados)):
    if a <= dados[i][0] <= b:
      df.iloc[i, 2] = "sim"
      m = m+1    

  print("número de maçãs:", m)
  plotar(df)
  return df

def verificaMacas1var(dados, a): # verifica quais frutas são maçãs de acordo com as cacterísticas estipuladas no intervalo [a, 10], que podem variar de 0 a 10.

  df = pd.DataFrame(dados, columns=['cor', 'formato', 'maçã?'])
  m=0
  
  for i in range(len(dados)):
    if dados[i][0] <= a:
      df.iloc[i, 2] = "sim"
      m = m+1

  print("número de maçãs:", m)
  plotar(df)
  return df

def plotar(df):

  range_max_y = (0, 10)

  # Check if each element meets the criteria for both X and Y ranges
  criteria = (df['maçã?'] == "sim") & (df['cor'].between(range_max_y[0], range_max_y[1]))

  # Plot the scatter plot using Matplotlib and different colors based on the criteria
  plt.scatter(df['cor'][criteria], df['formato'][criteria], color='red', marker='o', label='Meets Criteria')
  plt.scatter(df['cor'][~criteria], df['formato'][~criteria], color='blue', marker='o', label='Does Not Meet Criteria')
  plt.xlabel('formato')
  plt.ylabel('cor')
  plt.title('Scatter Plot with Color Criteria')
  plt.legend()
  plt.grid(True)
  plt.show()



def funcaoAprendizado(df, deslocamento, temperatura):

  acertos = 0
  pesos = random.uniform(0, 10) # peso inicial aleatório entre 0 e 10
  
  for numFruta in range(len(df)):
    formatoX = df.iloc[numFruta, 1]
    entradas = [formatoX]

    pesos = [random.uniform(0, 10)] # peso aleatório temporário

    resposta = neuronio(entradas, pesos, deslocamento, temperatura)
    resultado = verificaResposta(resposta, numFruta, df)
    print("acertou?:", resultado,"\n")
    if resultado == True:
      acertos = acertos+1

  porcentagemAcertos = acertos*100/len(df)
  print("Porcentagem de acertos:", porcentagemAcertos, "%")

def verificaResposta(resposta, numFruta, df):

  print("Linha:", df.iloc[[numFruta]])

  if resposta == True:
    if df.iloc[numFruta, 2] == 'sim':
      return True # Verdadeiro Verdadeiro
    else:
      print("falso positivo")
      return False # Verdadeiro Falso (falso positivo)
    
  else:
    if df.iloc[numFruta, 2] == 'sim':
      print("falso negativo")
      return False # Falso Verdadeiro (falso negativo)
    else:
      return True # Falso Falso



def main():

  # verificaEntradasEpesos(entradas, pesos)
  
# # definição de maçã 2 var:
  # range cor:
  a = 2
  b = 7 

  # range formato:
  c = 4
  d = 8
  
  quantidadeFrutas = 10
  frutas = criaFrutas(quantidadeFrutas)
  # verificaMacas4var(frutas, a,b, c,d)
  # verificaMacas2var(frutas, a,b)

  df = verificaMacas1var(frutas, a)
  funcaoAprendizado(df, deslocamento, temperatura)




  # separar parte do DF para aprendizado e outra parte para teste

  # neuronio(entradas, pesos, deslocamento, temperatura)


main()
