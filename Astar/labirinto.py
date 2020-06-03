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
        self.prioridade =99999999


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
        print(data)
        return labirinto(data)
    except:
        return None
    finally:
        try:
            f.close() #fecha o arquivo
        except:
            pass

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
        for item in caminho:
            data.append(item)
            a(direcao(prev, item))
            prev = item
        #print(" -> ".join(caminhoCompleto))
        a("Fim")
    return result, tempoTotal, data
