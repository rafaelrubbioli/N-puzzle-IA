from copy import deepcopy
from Node import Node
import time
import testBoards

# busca em largura
def breadth_first_search(node):
    frontier = [node]
    explored = []

    while True:
        if len(frontier) == 0:
            print("Nao encontrou resultado")
            return False

        node = frontier.pop(0)
        explored.append(node)
        possibleActions = node.possibleActions()

        for action in possibleActions:
            child = Node(deepcopy(node.board), node.empty, node.solution)
            child.switch(action)
            child.last = node

            if child.isOk():
                print("Solucao encontrada - ", child.solution + 1)
                return True

            if not alreadyContains(explored, child) and not alreadyContains(frontier, child):
                child.solution = child.solution + 1
                frontier.append(child)


# busca limitada em tamanho crescente
def iterative_deepening_search(node):
    depth = 0

    while True:
        result = depth_first_search(depth, node)
        if result != -1:
            print("Solucao encontrada - ", result)
            return True
        depth = depth + 1


# busca em profundidade limitada
def depth_first_search(limit, node):
    if node.isOk():
        return node.solution

    if limit == 0:
        return -1

    cutoff_occurred = False
    actions = node.possibleActions()
    for action in actions:
        child = Node(deepcopy(node.board), node.empty, node.solution + 1)
        child.switch(action)
        child.last = node

        result = depth_first_search(limit - 1, child)
        if result == -1:
            cutoff_occurred = True

        else:
            return result

    if cutoff_occurred:
        return -1

    else:
        return -2


# busca de custo uniforme
def uniform_cost_search(node):
    frontier = [node]
    explored = []

    while True:
        if len(frontier) == 0:
            print("Nao encontrou resultado")
            return False

        lowestCost = -1
        position = -1
        for i in range(len(frontier)):
            if lowestCost == -1 or frontier[i].solution < lowestCost:
                lowestCost = frontier[i].solution
                position = i

        node = frontier.pop(position)
        explored.append(node)
        possibleActions = node.possibleActions()

        for action in possibleActions:
            child = Node(deepcopy(node.board), node.empty, node.solution)
            child.switch(action)
            child.last = node

            if child.isOk():
                print("Solucao encontrada - ", child.solution + 1)
                return True

            if not alreadyContains(explored, child) and not alreadyContains(frontier, child):
                child.solution = child.solution + 1
                frontier.append(child)


# busca A*
def a_star_search(node):
    frontier = []
    explored = []
    n = node
    index = -1
    while True:
        explored.append(n.board)
        if n.isOk():
            print("Solucao encontrada - ", n.solution)
            return n

        for action in n.possibleActions():
            child = Node(deepcopy(n.board), n.empty, n.solution + 1)
            child.switch(action)
            child.last = n
            if child.board not in explored:
                frontier.append(child)

            if child.isOk():
                print("solucao encontrada - ", child.solution)
                return child

        lowest = -1
        for i in range(len(frontier)):
            if frontier[i].cost == -1:
                frontier[i].cost = frontier[i].numberOfWrongPieces()
            else:
                frontier[i].cost = frontier[i].numberOfWrongPieces() + frontier[i].cost

            if (lowest == -1 or frontier[i].cost <= lowest) and frontier[i].board not in explored:
                lowest = frontier[i].cost
                n = frontier[i]
                index = i

        frontier.pop(index)


# busca gulosa com heuristica
def greedy_best_first_search(node):
    frontier = []
    explored = []
    n = node
    index = -1
    while True:
        explored.append(n.board)
        if n.isOk():
            print("Solucao encontrada - ", n.solution)
            return n

        for action in n.possibleActions():
            child = Node(deepcopy(n.board), n.empty, n.solution + 1)
            child.switch(action)
            child.last = n
            if child.board not in explored:
                frontier.append(child)

            if child.isOk():
                print("solucao encontrada - ", child.solution)
                return child

        lowest = -1
        for i in range(len(frontier)):
            if frontier[i].cost == -1:
                frontier[i].cost = frontier[i].numberOfWrongPieces()

            if (lowest == -1 or frontier[i].cost <= lowest) and frontier[i].board not in explored:
                lowest = frontier[i].cost
                n = frontier[i]
                index = i

        frontier.pop(index)


# busca hill climbing
def hill_climbing_search(node):
    explored = []
    node.cost = node.numberOfWrongPieces()
    while True:
        explored.append(node.board)
        if node.isOk():
            print("Solucao encontrada", node.solution)
            return node

        frontier = []
        newnode = None
        lowest = node.cost
        for action in node.possibleActions():
            child = Node(deepcopy(node.board), node.empty, node.solution + 1)
            child.switch(action)
            child.last = node
            child.cost = child.numberOfWrongPieces()

            if child.board not in explored:
                frontier.append(child)
                if child.cost <= lowest:
                    lowest = child.cost
                    newnode = child

        if not newnode:
            if len(frontier) > 0:
                lowest = frontier[0].cost
                newnode = frontier[0]
                for child in frontier:
                    if child.cost < lowest:
                        lowest = child.cost
                        newnode = child

        if not newnode:
            print("Travei")
            return None

        node = newnode


# checa se o elemento ja esta contido na lista
def alreadyContains(list, node):
    for element in list:
        if element.equals(node):
            return True
    return False


# inicializa o jogo e cria o tabuleiro inicial
def initialize():
    print("Bem vindo ao N-Puzzle!")
    tipo = input("1) Tabuleiro existente\n2) Digitar novo jogo\n")
    board = []
    empty = None

    if tipo == "2":
        n = input("Qual o tamanho desejado? ( tamanho x tamanho ): ")
        size = int(n)
        for i in range(size):
            line = input("Digite as casas da linha "
                         + str(i + 1) + " ( separando com ' ' e coloque um 0 onde nao ha ): ")
            line = str.split(line, " ")
            for j in range(size):
                line[j] = int(line[j])
                if line[j] == 0:
                    empty = (i, j)
            board.append(line)

    if tipo == "1":
        n = input("Numero do tabuleiro: ")
        board, empty = testBoards.get(int(n))

    node = Node(board, empty, 0)
    print("Tabuleiro: ")
    node.show()
    return node


def main():
    node = initialize()

    tipo = input(
        "Escolha qual jogador deseja testar:"
        "\n1- BFS\n2- IDS\n3- Uniform Cost\n4- A estrela\n5- Greedy Best\n6- Hill Climbing\n"
    )
    tipo = int(tipo)

    if node.isOk():
        print("Esta pronto!")
        print("Solucao - ", node.solution)
    else:
        start = time.time()
        if tipo == 1:
            print("Comecando o BFS ...")
            breadth_first_search(node)
        elif tipo == 2:
            print("Comecando o IDS ...")
            iterative_deepening_search(node)
        elif tipo == 3:
            print("Comecando o uniform cost ...")
            uniform_cost_search(node)
        elif tipo == 4:
            print("Comecando o A estrela ...")
            a_star_search(node)
        elif tipo == 5:
            print("Comecando o greedy best ...")
            greedy_best_first_search(node)
        elif tipo == 6:
            print("Comecando o hill climbing ...")
            hill_climbing_search(node)
        end = time.time()
        print("Execucao em - ", end-start)


if __name__ == '__main__':
    main()
