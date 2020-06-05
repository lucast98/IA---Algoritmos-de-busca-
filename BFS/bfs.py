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


def BFS(lab, estAtual, estFinal):
  explored = []
  queue = [[estAtual]]

  while queue:
    path = queue.pop(0)
    node = path[-1]

    if node not in explored:
      neighbors = getNeighbors(len(lab.data), len(lab.data[0])-1, node)

      for n in neighbors:
        if lab.data[n[0]][n[1]] > 0:
          new_path = list(path)
          new_path.append(n)
          queue.append(new_path)

          if n == estFinal:
            return new_path

      explored.append(node)

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
      caminho = BFS(lab, estAtual, estFinal)
      tempoFim = time.time()

      tempo.append(tempoFim - tempoInicio)
      print('Caminho Encontrado!\n', caminho)

      rep += 1

    plotLabirinto(lab.data, caminho, lab.linha, lab.coluna)
    print(Fore.WHITE + "Tempo médio de execução: ", np.mean(tempo), "segundos")
