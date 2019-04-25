from copy import deepcopy
from Node import Node
import time

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


# busca em profundidade
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


# busca a estrela
def a_star_search(node):
    pass


# busca gulosa
def greedy_best_first_search(node):
    frontier = []
    while True:
        for action in node.possibleActions()
        lowest = -1
        for item in frontier:
            cost = item.numberOfWrongPieces()
            if lowest == -1 or cost < lowest:
                lowest = cost


# busca hill climbing
def hill_climbing_search(node):
    pass


# checa se o elemento ja esta contido na lista
def alreadyContains(list, node):
    for element in list:
        if element.equals(node):
            return True
    return False


# inicializa o jogo e cria o tabuleiro inicial
def initialize():
    print("Bem vindo ao N-Puzzle!")
    n = input("Qual o tamanho desejado? ( tamanho x tamanho ): ")
    size = int(n)
    board = []
    empty = None
    for i in range(size):
        line = input("Digite as casas da linha "
                     + str(i + 1) + " ( separando com ' ' e coloque um 0 onde nao ha ): ")
        line = str.split(line, " ")
        for j in range(size):
            line[j] = int(line[j])
            if line[j] == 0:
                empty = (i, j)
        board.append(line)

    node = Node(board, empty, 0)
    print("Tabuleiro: ")
    node.show()
    return node


def main():
    #node = initialize()
    # teste 2
    #node = Node([[1, 2, 3], [4, 0, 5], [7, 8, 6]], (1, 1), 0)
    # teste 7
    #node = Node([[1, 5, 2], [4, 8, 0], [7, 6, 3]], (1, 2), 0)
    # teste 31
    node = Node([[8, 7, 6], [2, 5, 4], [3, 0, 1]], (2, 1), 0)


    tipo = input(
        "Escolha qual jogador deseja testar:"
        "\n1- BFS\n2- DFS\n3- Uniform Cost\n4- A estrela\n5- Greedy Best\n6- Hill Climbing\n"
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
            print("Comecando o DFS ...")
            iterative_deepening_search(node)
        elif tipo == 3:
            print("Comecando o uniform cost")
            uniform_cost_search(node)
        elif tipo == 4:
            print("Comecando o A estrela")
            a_star_search(node)
        elif tipo == 5:
            print("Comecando o greedy best")
            greedy_best_first_search(node)
        elif tipo == 6:
            print("Comecando o hill climbing")
            hill_climbing_search(node)
        end = time.time()
        print("Execucao em - ", end-start)

if __name__ == '__main__':
    main()
