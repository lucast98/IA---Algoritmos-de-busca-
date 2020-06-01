from math import sqrt
from labirinto import main, listLabirinto, plotLabirinto

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

def getDistance(est, estFinal):
  return sqrt((estFinal[0] - est[0])**2 + (estFinal[1] - est[1])**2)

def selectionSort(A, estFinal):
  for i in range(len(A)):
    min_idx = i

    for j in range(i+1, len(A)):
      if getDistance(A[min_idx], estFinal) > getDistance(A[j], estFinal):
        min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

def DFS(lab, estAtual, estFinal, caminho):
  caminho.append(estAtual)
  neighbors = getNeighbors(len(lab.data), len(lab.data[0])-1, estAtual)
  selectionSort(neighbors, estFinal)

  for n in neighbors:
    if estFinal not in caminho:
      if lab.data[n[0]][n[1]] > 0 and n not in caminho:
        DFS(lab, n, estFinal, caminho)

  if estFinal not in caminho:
    caminho.pop()

if __name__ == '__main__':
    lab = listLabirinto("labirinto.txt")
    estAtual = lab.estInicial
    estFinal = lab.estFinal
    caminho = []

    DFS(lab, estAtual, estFinal, caminho)

    print(caminho)

    for line in lab.data:
      print(line)

    plotLabirinto(lab.data, caminho, lab.linha, lab.coluna)
