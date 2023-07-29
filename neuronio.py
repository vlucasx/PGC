import math

entradas = [3,0.2,0.6] # vetor de entrada 
pesos = [0.1,0.3,0.4] # vetor de pesos
deslocamento = 0
temperatura = 0.001  # 0.001 forma um degrau razoável

def verificaEntradasEpesos(entradas, pesos): # verifica se a quantidade de entradas e de pesos é igual
  if len(entradas) > len(pesos):
    print("vetor de entradas maior que o de pesos")
    return
  elif len(entradas) < len(pesos):
    print("vetor de entradas menor que o de pesos")
    return
  return True

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
  
  if net > funcaoAtivacao(net,deslocamento,temperatura): # Se x > f(X), o neurônio ativa sua saída. Se x >= f(x) não ativa a saída.
      print("ativou: f("+str(net)+") = "+str(funcaoAtivacao(net,deslocamento,temperatura)))
      return False
  else:
    print("não ativou: f("+str(net)+") = "+str(funcaoAtivacao(net,deslocamento,temperatura)))
    return True

def main():
  if not verificaEntradasEpesos(entradas, pesos):
    return

  neuronio(entradas, pesos, deslocamento, temperatura)


main()
