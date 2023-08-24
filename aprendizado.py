matrizEntradas =  [[1,-1, 1,-1],
                 [1, 1, 1, 1]]
pesos = [-1,-1,0,0]
target = [1, 1]
aprendizado = 0.25

def calculaNet(entradas, pesos):
    if len(entradas) != len(pesos):
        print("tamanho entradas diferente de pesos")
        exit()

    net = 0
    i=0   
    for a in entradas:   
        net = net+a*pesos[i]
        i=i+1

    return net


def verificaLimiar(net, limiar):
    if net > limiar:
        return 1
    return 0

def aprender(matrizEntradas, pesos, target, aprendizado):
    i=0
    novoPeso = []

    print("vetor entradas:", matrizEntradas)
    print("pesos:", pesos)
    print("target:", target)
    print("")
    erro = []
    print("tam vetor entradas:", len(matrizEntradas))
    print("tam vetor target:", len(target))

    res = 0
    while i < 30:

        print("")
        print("Época ", i,"===========================:")

        k=0
        for entradas in matrizEntradas:
            net = calculaNet(entradas, pesos)
            print("net:", net)
            print("target:", target)

            output = verificaLimiar(net,0)
            erro.append(target[k]-output)
            print("output:", output)
            print("erro:", erro[k])
            print("")
            j=0
            auxNovoPeso = []
            for peso in pesos:
                auxNovoPeso.append(pesos[j] + erro[k]*aprendizado*entradas[j])
                j=j+1

            pesos = auxNovoPeso
            print("novos pesos:", pesos)
            print("")

            k=k+1
        
        for e in erro:
            if e == 0:
                res = res+1
        
        if res == len(erro):
            exit()

        erro = []
        res = 0
        i=i+1


aprender(matrizEntradas, pesos, target, aprendizado)