from labirinto import main, listLabirinto, plotLabirinto

class posicao():
    def __init__(self,a,b,c):
        self.prioridade=a
        self.linha=b
        self.coluna=c
    def get_prioridade(self):
        return self.prioridade
    
class priorityQueue():
    def __init__(self):
        self.PQ = list()
        self.ordenado =True
    def add(self,posicao):
        self.PQ.append(posicao)
        self.ordenado =False
    def pop(self):
        if self.ordenado == False:
            self.PQ.sort(self.PQ, key = posicao.get_prioridade(self),reverse=True)
            ordenado=True
        ret= PQ[0]
        self.PQ[0].remove()
        return ret

def getNeighbors(rows, columns, row,column):
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

def heuristica(estFinal, estAtual, estPossivel):
        atual = abs(estFinal[0] - estAtual[0]) + abs(estFinal[1] - estAtual[1])
        possivel = abs(estFinal[0] - estPossivel[0]) + abs(estFinal[1] - estPossivel[1])
        return atual + possivel


def Astar(lab, estInicial, estFinal):
    caminho=[]
    PQ = priorityQueue()
    PQ.add((heuristica(estFinal,estInicial,estInicial),estAtual))
    
    while PQ:
        node = PQ.pop()
        neighbors = getNeighbors(len(lab.data), len(lab.data[0])-1, node[0],node[1])
        
        for n in neighbors:
            if lab.data[n[0]][n[1]] > 0:
                   PQ.add(heuristica(estFinal,estAtual,lab.data),estAtual)
                   
                   if n == estFinal:
                       caninho.add(estFinal)
                       node = node.pai()
                       
                       while node != estInicial:
                           caminho.add(node)
                           node = node.pai()
                       
                       caminho.add(estInicial)
        #node.pri=9999999

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
