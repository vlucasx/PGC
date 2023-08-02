import math

entradas = [4,0.5,1.1] # vetor de entrada 
pesos = [0.1,0.3,0.4] # vetor de pesos
deslocamento = 1 # deslocamento inicial +1 para direita para que f(x>1) = 1
temperatura = 0.0001  # 0.0001 forma um degrau razoável

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

def main():
  verificaEntradasEpesos(entradas, pesos)
  

  neuronio(entradas, pesos, deslocamento, temperatura)


main()
