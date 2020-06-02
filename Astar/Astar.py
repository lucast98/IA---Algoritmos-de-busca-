from labirinto import main, listLabirinto, plotLabirinto, heuristica
from queue import PriorityQueue

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


def Astar(lab, estAtual, estFinal):
    explored = []
    PQ =PriorityQueue()
    PQ.put(heuristica(estAtual,estAtual),estAtual)

    while PQ:
        path = PQ.pop()
        node = path[-1]

        if node not in explored:
            neighbors = getNeighbors(len(lab.data), len(lab.data[0])-1, node)

            for n in neighbors:
                if lab.data[n[0]][n[1]] > 0:
                    new_path = list(path)
                    new_path.append(n)
                    PQ.put(heuristica(estAtual,lab.data),estAtual)

                    if n == estFinal:
                        return new_path

            explored.append(node)

if __name__ == '__main__':
    lab = listLabirinto("labirinto.txt")
    estAtual = lab.estInicial
    estFinal = lab.estFinal
    caminho = []

    caminho = Astar(lab, estAtual, estFinal)

    print(caminho)

    for line in lab.data:
      print(line)

    plotLabirinto(lab.data, caminho, lab.linha, lab.coluna)
