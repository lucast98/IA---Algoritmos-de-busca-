import sys, random
from labirinto import main, listLabirinto, plotLabirinto
from math import e
import numpy as np
import colorama
import heapq
from colorama import Fore, Back, Style

'''Classe nó'''
class no:
    __slots__ = ['estado', 'prox']

    def __init__(self, estado, prox = None):
        self.estado = estado
        self.prox = prox

    def __eq__(self, outro):
        if(isinstance(outro, no)): #verifica se o outro é um nó
            return self.estado == outro.estado
        elif(isinstance(outro, tuple)): #verifica se é uma tupla
            return self.estado == outro
        return False 

''' Classe que representa listas '''
class lista:
    def __init__(self):
        self.q = []

    #insere elementos na fila de prioridades
    def push(self, elem):
        heapq.heappush(self.q, elem)

    #retira elementos da fila de prioridades
    def pop(self):
        return heapq.heappop(self.q)

    #verifica se estado é melhor ou nao
    def melhor(self, custo, estado):
        for custoAcao, estadoAcao in self.q:
            if estadoAcao == estado:
                if custoAcao <= custo:
                    return True
                else:
                    return False
        return False

''' Classe que monta o caminho'''
class Caminho:
    def __init__(self, estInicial):
        self.lista = [no(estInicial)]

    #adiciona elemento a lista que representa o caminho percorrido
    def add(self, estado, prox):
        for i in self.lista:
            if i == prox:
                prox = i
                break
        self.lista.append(no(estado, prox))

    #concatena o caminho até o estado final, e depois reverte
    def montaCaminho(self):
        n = self.lista[-1]
        path = [] #caminho vazio
        while(n):
            path.append(n.estado) #concantena estados
            n = n.prox #vai para o proximo
        path.reverse() #inverte o caminho, para que tenha da entrada até a saída
        return path

''' Função que utiliza o algoritmo A* '''
def Astar(labirinto):
    caminho = Caminho(labirinto.estInicial) #instância do caminho
    aberta = lista() #cria lista aberta
    fechada = lista() #cria lista fechada
    aberta.push((0, labirinto.estInicial)) #insere o estado inicial na lista aberta
    estFinal = labirinto.estFinal #obtem estado final
    while aberta.q:
        g, q = aberta.pop() #g é o custo de movimento, enquanto q é o nó com menor 'f'
        for estado in labirinto.proxEst(q):
            if estado == estFinal:
                caminho.add(estado, q)
                return caminho.montaCaminho(), 1 #retorna o caminho e o valor 1 se encontrou caminho
            h = labirinto.heuristica(estado) #heuristica (manhattan distance)
            f = g + h 
            if aberta.melhor(f, estado): #verifica qual estado é o melhor 
                continue
            if fechada.melhor(f, estado): #verifica qual estado é o melhor
                continue
            caminho.add(estado, q) #adiciona nó ao caminho
            aberta.push((f, estado)) #insere nó na lista aberta
        fechada.push((g, q)) #insere nó na lista fechada
    return caminho.montaCaminho(), 0 #nao chegara aqui, pois o a* sempre encontra o caminho


if __name__ == '__main__':
    n = 100
    tempo = []
    lab = listLabirinto("labirinto.txt") #obtem labirinto a partir do arquivo texto
    rep = 0 #numero de repetições
    while rep <= n: #repete n vezes para obter a media do tempo de execução
        sucesso, tempo_aux, finalData = main(Astar, lab)
        if sucesso == 1:
            rep = rep + 1 #incrementa numero de repetições
            tempo.append(tempo_aux) #lista com tempo de execução do algoritmo
    data = np.random.rand(lab.coluna, lab.linha) * 20
    plotLabirinto(lab.data, finalData, lab.linha, lab.coluna)
    #print("Tempo médio de execução: ", np.mean(tempo), "segundos")
    colorama.init()
    print(Fore.WHITE + "Tempo médio de execução: ", np.mean(tempo), "segundos")