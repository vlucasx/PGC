import math

entradas = [3,0.2,0.6] # vetor de entrada 
pesos = [0.4,0.5,0.5] # vetor de pesos
limiarAtivacao = 1 # threshold (posteriormentte uma função)

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

def neuronio(entradas, pesos, limiarAtivacao): # método do neurônio
  net = 0
  i=0

# calcula o valor de rede (net)
  for entrada in entradas:
    net = net + entrada * pesos[i]
    i=i+1
    
  print("Limiar:", limiarAtivacao)
  print("Net:", net)
  print("")

# verifica se o neurônio disparou
  if net >= limiarAtivacao:
    print("DISPAROU (Net >= Limiar)")
  else:
    print("Não disparou (Net < Limiar)")


def main():
  if not verificaEntradasEpesos(entradas, pesos):
    return
  neuronio(entradas, pesos, limiarAtivacao)
  deslocamento = 0
  temperatura =-1

  for net in range(0,30):
    if net/10 > funcaoAtivacao(net/10,deslocamento,temperatura):
      print("ativado ", "f("+str(net/10)+") = "+str(funcaoAtivacao(net/10,deslocamento,temperatura)))
    else:
        print("f("+str(net/10)+") = "+str(funcaoAtivacao(net/10,deslocamento,temperatura)))

main()
