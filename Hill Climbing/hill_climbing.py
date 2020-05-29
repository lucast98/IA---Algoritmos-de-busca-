import sys, random
from labirinto import main, listLabirinto, plotLabirinto
from math import e
import numpy as np

#Função que utiliza o algoritmo Simple Hill Climbing
def hill_climbing(labirinto):
    estAtual = labirinto.estInicial #estado inicial
    estFinal = labirinto.estFinal #estado final
    caminho = [estAtual]
    while estAtual != estFinal:
        found = False
        for est in labirinto.proxEst(estAtual):
            if labirinto.verMelhor(est, estAtual): #verifica se o novo estado é melhor e, se for, anexa ao caminho já percorrido
                #print(est)
                caminho.append(est)
                estAtual = est #atual é o novo estado
                found = True #encontrou um estado melhor
                break
        if found:
            continue
        return caminho, 0 #nao encontrou solucao
    return caminho, 1 #encontrou solucao

#Função que define a probabilidade de realizar um movimento com base na 'temperatura'
def prob(dE, T):
    try:
        k = 1e-2
        exp = - (dE / (T*k))
        return e**exp
    except:
        return 200 #volta a temperatura inicial

#Função que utiliza o algoritmo Simulated Annealing
def simulated_annealing(labirinto):
    estAtual = labirinto.estInicial #Posição da entrada do labirinto
    estFinal = labirinto.estFinal #Posição da saida do labirinto
    caminho = [estAtual] #Caminho
    caminhoTeste = [] #Caminho de teste
    T = 200 #'Temperatura'
    ant = None #Nó anterior ainda não existe
    while estAtual != estFinal:
        found = False #Não encontrou a saída
        E1 = labirinto.heuristica(estAtual) #valor heuristico do estado atual
        P = True
        for est in labirinto.proxEst(estAtual):
            if P:
                P = False
            if est == ant: #não é pra continuar no mesmo lugar
                continue
            E2 = labirinto.heuristica(est) #valor heuristico do novo estado
            if est == estFinal:
                caminho.append(est) #anexa a posicao nova ao que já foi explorado
                return caminho, 1 #encontrou solucao
            if labirinto.verMelhor(est, estAtual): #verifica se estado novo é melhor que o atual
                caminho.extend(caminhoTeste)
                caminho.append(est) #novo estado faz parte da solução
                caminhoTeste = [] #caminho teste fica vazio pq encontrou um que já serve
                ant = estAtual #anterior é o atual
                estAtual = est #novo atual é o proximo
                found = True #encontrou um novo estado melhor
                break
            else:
                p = prob(E2-E1, T)
                if p < random.random(): #define aleatoriedade das escolhas
                    found = True #encontrou um estado valido
                    caminhoTeste.append(est) #novo estado faz parte da solução
                    ant = estAtual #anterior é o atual
                    estAtual = est #novo atual é o proximo
                    break
        if not found:
            return caminho, 0 #nao encontrou solucao
        T = 0.98*T #diminui temperatura
    return caminho, 1 #encontrou solucao

if __name__ == '__main__':
    n = 10
    tempo = []
    lab = listLabirinto("labirinto.txt") #obtem labirinto a partir do arquivo texto
    rep = 0 #numero de repetições
    while rep <= n: #repete n vezes para obter a media do tempo de execução
        sucesso, tempo_aux, finalData = main(simulated_annealing, lab)
        if sucesso == 1:
            rep = rep + 1 #incrementa numero de repetições
            tempo.append(tempo_aux) #lista com tempo de execução do algoritmo
    data = np.random.rand(lab.coluna, lab.linha) * 20
    plotLabirinto(lab.data, finalData, lab.linha, lab.coluna)
    print("Tempo médio de execução: ", np.mean(tempo))