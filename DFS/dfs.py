import time
import numpy as np
from labirinto import listLabirinto, plotLabirinto
from colorama import Fore

def getNeighbors(rows, columns, estAtual):
    row = estAtual[0]
    column = estAtual[1]
    neighbors = []

    if row == 0:
      if column == 0:
        neighbors.append((row, column+1))
        neighbors.append((row+1, column))

      if column > 0 and column < columns-1:
        neighbors.append((row, column-1))
        neighbors.append((row, column+1))
        neighbors.append((row+1, column))

      if column == columns-1:
        neighbors.append((row, column-1))
        neighbors.append((row+1, column))

    if row > 0 and row < rows-1:
      if column == 0:
        neighbors.append((row-1, column))
        neighbors.append((row, column+1))
        neighbors.append((row+1, column))

      if column > 0 and column < columns-1:
        neighbors.append((row-1, column))
        neighbors.append((row, column-1))
        neighbors.append((row, column+1))
        neighbors.append((row+1, column))

      if column == columns-1:
        neighbors.append((row-1, column))
        neighbors.append((row, column-1))
        neighbors.append((row+1, column))

    if row == rows-1:
      if column == 0:
        neighbors.append((row-1, column))
        neighbors.append((row, column+1))

      if column > 0 and column < columns-1:
        neighbors.append((row-1, column))
        neighbors.append((row, column-1))
        neighbors.append((row, column+1))

      if column == columns-1:
        neighbors.append((row-1, column))
        neighbors.append((row, column-1))

    return neighbors


def DFS(lab, estAtual, estFinal, caminho):
  caminho.append(estAtual)
  neighbors = getNeighbors(len(lab.data), len(lab.data[0])-1, estAtual)

  for n in neighbors:
    if estFinal not in caminho:
      if lab.data[n[0]][n[1]] > 0 and n not in caminho:
        DFS(lab, n, estFinal, caminho)

  if estFinal not in caminho:
    caminho.pop()


if __name__ == '__main__':
    n = 1
    tempo = []
    lab = listLabirinto("labirinto.txt") #obtem labirinto a partir do arquivo texto
    rep = 0 #numero de repetições

    while rep < n:
      estAtual = lab.estInicial
      estFinal = lab.estFinal
      caminho = []

      tempoInicio = time.time()
      DFS(lab, estAtual, estFinal, caminho)
      tempoFim = time.time()

      tempo.append(tempoFim - tempoInicio)
      print('Caminho Encontrado!\n', caminho)

      rep += 1

    plotLabirinto(lab.data, caminho, lab.linha, lab.coluna)
    print(Fore.WHITE + "Tempo médio de execução: ", np.mean(tempo), "segundos")
