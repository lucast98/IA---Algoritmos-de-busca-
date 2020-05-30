import matplotlib.pyplot as plt
import time
import numpy as np
import colorama
from colorama import Fore, Back, Style

class labirinto:
    def __init__(self, data):
        self.linha = len(data) #linha
        self.coluna = len(data[0]) #coluna
        self.data = data
        self.estInicial = (0, self.data[0].index(3))
        self.estFinal = (self.linha-1, self.data[self.linha-1].index(2))

    #Define o proximo estado
    def proxEst(self, estAtual):
        try:
            #vai para baixo
            if estAtual[0] != self.linha - 1:
                if estAtual != self.estFinal and self.data[estAtual[0] + 1][estAtual[1]] == 1:
                    yield (estAtual[0] + 1, estAtual[1])
            #vai para cima
            if estAtual[0] != 0:
                if estAtual != self.estInicial and self.data[estAtual[0] - 1][estAtual[1]] == 1:
                    yield (estAtual[0] - 1, estAtual[1])
            #vai para a direita
            if estAtual[1] != self.coluna - 1:
                if self.data[estAtual[0]][estAtual[1] + 1] == 1 or self.data[estAtual[0]][estAtual[1] + 1] == 2:
                    yield (estAtual[0], estAtual[1]+1)
            #vai para a esquerda
            if estAtual[1] != 0:
                if self.data[estAtual[0]][estAtual[1] - 1] == 1 or self.data[estAtual[0]][estAtual[1] - 1] == 2:
                    yield (estAtual[0], estAtual[1]-1)
        except:
            return None

    #Valor heuristico do estado (manhattan distance)
    def heuristica(self, est):
        return abs(self.estFinal[0] - est[0]) + abs(self.estFinal[1] - est[1])

    #Verifica se o novo estado é melhor que o atual
    def verMelhor(self, s1, s2, toprint = False):
        val1 = self.heuristica(s1)
        val2 = self.heuristica(s2)
        if val1 == val2:
            return s1[0] > s2[0]
        else:
            return bool(val1 < val2)

#Direções a serem tomadas no labirinto
def direcao(prev, cur):
    if cur[0] > prev[0]:
        return "Baixo"
    elif cur[0] < prev[0]:
        return "Cima"
    elif cur[1] > prev[1]:
        return "Direita"
    elif cur[1] < prev[1]:
        return "Esquerda"
    else:
        return "Inicio"

def listLabirinto(filename):
    try:
        f = open(filename, "r+") #abre o arquivo
        l = f.readlines() #le todas as linhas

        #Substitui:
         # # -> 3
         # $ -> 2
         # * -> 1
         # - -> 0
        data = [[3 if i == '#' else 2 if i == '$' else 1 if i == '*' else 0 for i in j] for j in l]
        data.pop(0) #remove a primeira linha da lista
        #print(data)
        return labirinto(data)
    except:
        return None
    finally:
        try:
            f.close() #fecha o arquivo
        except:
            pass

def preencheLabirinto(data, finalData):
    for i in range(0, len(finalData)):
        data[list(finalData[i])[0]][list(finalData[i])[1]] = 4

def plotLabirinto(data, finalData, linha, coluna):
    preencheLabirinto(data, finalData)
    colorama.init()
    for i in range(0, linha):
        for j in range(0, coluna-1):
            if data[i][j] == 0:
                print(Fore.RED + "-", end="")
            elif data[i][j] == 1:
                print(Fore.WHITE + "*", end="")
            elif data[i][j] == 2 or data[i][j] == 3 or data[i][j] == 4:   
                print(Fore.GREEN + "@", end="")      
        print("")

def main(function, lab):
    tempoInicio = time.time()
    caminho, result = function(lab)
    tempoFim = time.time()
    tempoTotal = (tempoFim - tempoInicio)
    caminhoCompleto = []
    data = []
    a = caminhoCompleto.append
    if result == 1:
        print("Caminho Encontrado!")
        prev = caminho[0]
        print(caminho)
        for item in caminho:
            data.append(item)
            a(direcao(prev, item))
            prev = item
    return result, tempoTotal, data
