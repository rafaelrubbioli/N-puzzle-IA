from copy import deepcopy
from Node import Node
import time
import testBoards

# busca em largura
def breadth_first_search(node):
    frontier = [node.string]
    frontierdict = {}
    frontierdict[node.string] = node
    explored = set()
    expanded = 0
    while True:
        if len(frontier) == 0:
            print("Nao encontrou resultado")
            return False

        nodestring = frontier.pop(0)
        node = frontierdict[nodestring]
        del frontierdict[node.string]
        expanded = expanded + 1
        explored.add(node.string)
        possibleActions = node.possibleActions()

        for action in possibleActions:
            child = Node(deepcopy(node.board), node.empty, node.solution)
            child.switch(action)
            ## DESCOMENTAR PARA VER SOLUCAO
            #child.last = node
            if child.isOk():
                print("Solucao encontrada: ", child.solution + 1,
                      "\nNos expandidos: ", expanded)
                ## DESCOMENTAR PARA VER SOLUCAO
                #child.showSolution()
                return True

            if child.string not in explored and child.string not in frontier:
                child.solution = child.solution + 1
                frontier.append(child.string)
                frontierdict[child.string] = child


# busca limitada em tamanho crescente
def iterative_deepening_search(node):
    depth = 0
    while True:
        result = depth_first_search(depth, node)
        if result != -1:
            print("Solucao encontrada - ", result,
                  "\nNos expandidos ", expanded,
                  "\nNo limite ", depth)
            return True
        depth = depth + 1


expanded = 0 # global para o IDS


# busca em profundidade limitada
def depth_first_search(limit, node):
    global expanded
    expanded = expanded + 1
    if node.isOk():
        return node.solution

    if limit == 0:
        return -1

    cutoff_occurred = False
    actions = node.possibleActions()
    for action in actions:
        child = Node(deepcopy(node.board), node.empty, node.solution + 1)
        child.switch(action)
        #child.last = node
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
    frontier = [node.string]
    frontierdict = {}
    frontierdict[node.string] = node
    explored = set()
    expanded = 0
    while True:
        if len(frontier) == 0:
            print("Nao encontrou resultado")
            return False

        lowestCost = -1
        position = -1
        for i in range(len(frontier)):
            sol = frontierdict[frontier[i]].solution
            if lowestCost == -1 or sol < lowestCost:
                lowestCost = sol
                position = i

        nodestring = frontier.pop(position)
        node = frontierdict[nodestring]
        del frontierdict[node.string]
        expanded = expanded + 1
        explored.add(node.string)
        possibleActions = node.possibleActions()

        for action in possibleActions:
            child = Node(deepcopy(node.board), node.empty, node.solution)
            child.switch(action)
            ## DESCOMENTAR SE QUISER VER A SOLUCAO
            #child.last = node

            if child.isOk():
                print("Solucao encontrada: ", child.solution + 1,
                      "\nNos expandidos: ", expanded)
                ## DESCOMENTAR SE QUISER VER A SOLUCAO
                #child.showSolution()
                return True

            if child.string not in explored and child.string not in frontier:
                child.solution = child.solution + 1
                frontier.append(child.string)
                frontierdict[child.string] = child


# busca A*
def a_star_search(node):
    frontier = []
    explored = set()
    n = node
    index = -1
    expanded = 0
    while True:
        explored.add(n.string)
        if n.isOk():
            print("Solucao encontrada - ", n.solution,
                  "\nNos expandidos: ", expanded)
            ## DESCOMENTAR SE QUISER VER A SOLUCAO
            #n.showSolution()
            return n

        for action in n.possibleActions():
            child = Node(deepcopy(n.board), n.empty, n.solution + 1)
            child.switch(action)
            ## DESCOMENTAR SE QUISER VER A SOLUCAO
            child.last = n
            child.depth = n.depth + 1
            if child.string not in explored:
                frontier.append(child)

        lowest = -1
        for i in range(len(frontier)):
            if frontier[i].cost == -1:
                frontier[i].cost = frontier[i].manhattanDistance() + frontier[i].depth

            if (lowest == -1 or frontier[i].cost <= lowest) and frontier[i].string not in explored:
                lowest = frontier[i].cost
                n = frontier[i]
                index = i

        frontier.pop(index)
        expanded = expanded + 1


# busca gulosa com heuristica
def greedy_best_first_search(node):
    frontier = []
    explored = set()
    n = node
    index = -1
    expanded = 0
    while True:
        explored.add(n.string)
        if n.isOk():
            print("Solucao encontrada - ", n.solution,
                  "\nNos expandidos: ", expanded)
            ## DESCOMENTAR SE QUISER VER A SOLUCAO
            #n.showSolution()
            return n

        for action in n.possibleActions():
            child = Node(deepcopy(n.board), n.empty, n.solution + 1)
            child.switch(action)
            child.last = n
            if child.string not in explored:
                frontier.append(child)

        lowest = -1
        for i in range(len(frontier)):
            if frontier[i].cost == -1:
                frontier[i].cost = frontier[i].numberOfWrongPieces()

            if (lowest == -1 or frontier[i].cost <= lowest) and frontier[i].string not in explored:
                lowest = frontier[i].cost
                n = frontier[i]
                index = i

        frontier.pop(index)
        expanded = expanded + 1


# busca hill climbing
def hill_climbing_search(node):
    explored = []
    node.cost = node.numberOfWrongPieces()
    expanded = 0
    while True:
        explored.append(node.string)
        if node.isOk():
            print("Solucao encontrada", node.solution,
                  "\nNos expandidos: ", expanded)
            return node

        frontier = []
        newnode = None
        lowest = node.cost
        for action in node.possibleActions():
            child = Node(deepcopy(node.board), node.empty, node.solution + 1)
            child.switch(action)
            child.last = node
            child.cost = child.numberOfWrongPieces()

            if child.string not in explored:
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
        expanded = expanded + 1


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

    list = []
    for line in board:
        for item in line:
            list.append(item)

    slot= 3*empty[0] + empty[1]
    node = Node(list, slot, 0)
    print("Tabuleiro: ")
    node.show()
    return node

# teste
def test():
    ## TEST GREEDY
    # for i in range(31):
    #     board, empty = testBoards.get(int(i+1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     greedy_best_first_search(node)
    #     end = time.time()
    #     print("Execucao em - ", end - start)
    #
    ## TEST A*
    # for i in range(31):
    #     board, empty = testBoards.get(int(i+1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     a_star_search(node)
    #     end = time.time()
    #     print("Execucao em - ", end - start)
    #
    ## TEST HILL CLIMBING
    # for i in range(31):
    #     board, empty = testBoards.get(int(i + 1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     sol = hill_climbing_search(node)
    #     if sol:
    #         print("Solucao encontrada:")
    #         sol.showSolution()
    #         sol.showSolution()
    #     end = time.time()
    #     print("Execucao em - ", end - start)
    #
    ## TEST BFS
    # for i in range(31):
    #     board, empty = testBoards.get(int(i+1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     breadth_first_search(node)
    #     end = time.time()
    #     print("Execucao em - ", end - start)
    #
    ## TEST UNIFORM COST
    # for i in range(31):
    #     board, empty = testBoards.get(int(i+1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     uniform_cost_search(node)
    #     end = time.time()
    #     print("Execucao em - ", end - start)
    #
    ## TEST IDS
    # for i in range(31):
    #     board, empty = testBoards.get(int(i+1))
    #     list = []
    #     for line in board:
    #         for item in line:
    #             list.append(item)
    #
    #     slot = 3 * empty[0] + empty[1]
    #     node = Node(list, slot, 0)
    #
    #     start = time.time()
    #     iterative_deepening_search(node)
    #     end = time.time()
    #     print("Execucao em - ", end - start)

    pass

def main():
    ## DESCOMENTAR PARA USAR A FUNCAO DE TESTE
    # test()
    # return
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
            sol = hill_climbing_search(node)
            if sol:
                print("Solucao encontrada:")
                sol.showSolution()

        end = time.time()
        print("Execucao em - ", end-start)


if __name__ == '__main__':
    main()
