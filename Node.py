class Node:
    def __init__(self, board, empty, solution):
        self.board = board
        self.empty = empty
        self.solution = solution
        self.last = None
        self.size = len(self.board)
        self.cost = -1

    # troca as duas casas indicadas
    def switch(self, piece):
        self.board[self.empty[0]][self.empty[1]] = self.board[piece[0]][piece[1]]
        self.board[piece[0]][piece[1]] = 0
        self.empty = piece

    # transforma o tabuleiro em string para o explored
    def toString(self):
        boardString = ""
        for line in self.board:
            for item in line:
                boardString = boardString + str(item)

        return boardString

    # imprime o tabuleiro na tela
    def show(self):
        for line in self.board:
            print(line)
        print()

    # verifica se o jogo ja terminou
    def isOk(self):
        expected = 1
        for line in self.board:
            for item in line:
                if expected == 9:
                    if item != 0:
                        return False
                    else:
                        return True
                if item != expected:
                    return False
                expected = expected + 1

    # busca quais sao as opcoes de movimento
    def possibleActions(self):
        empty = self.empty
        end = len(self.board[0]) - 1

        possibleActions = []
        # primeira casa da primeira coluna
        if empty == (0,0):
            possibleActions.append((0,1))
            possibleActions.append((1,0))

        # ultima da primeira linha
        elif empty == (0, end):
            possibleActions.append((0, end - 1))
            possibleActions.append((1, end))

        # primeira casa da ultima linha
        elif empty == (end, 0):
            possibleActions.append((end, 1))
            possibleActions.append((end - 1, 0))

        # ultima casa da ultima linha
        elif empty == (end, end):
            possibleActions.append((end - 1, end))
            possibleActions.append((end, end - 1))

        # meio da primeira linha
        elif empty[0] == 0:
            possibleActions.append((0, empty[1] + 1))
            possibleActions.append((0, empty[1] - 1))
            possibleActions.append((1, empty[1]))

        # meio da ultima linha
        elif empty[0] == end:
            possibleActions.append((end, empty[1] + 1))
            possibleActions.append((end, empty[1] - 1))
            possibleActions.append((end - 1, empty[1]))

        # meio da lateral esquerda
        elif empty[1] == 0:
            possibleActions.append((empty[0] + 1, 0))
            possibleActions.append((empty[0] - 1, 0))
            possibleActions.append((empty[0], 1))

        # meio da lateral direita
        elif empty[1] == end:
            possibleActions.append((empty[0] + 1, end))
            possibleActions.append((empty[0] - 1, end))
            possibleActions.append((empty[0], end - 1))

        # meio do tabuleiro
        else:
            possibleActions.append((empty[0] + 1, empty[1]))
            possibleActions.append((empty[0] - 1, empty[1]))
            possibleActions.append((empty[0], empty[1] + 1))
            possibleActions.append((empty[0], empty[1] - 1))

        return possibleActions

    # heuristica para calcular quantas casas estao erradas
    def numberOfWrongPieces(self):
        wrongPieces = 0
        expected = 1
        for line in self.board:
            for item in line:
                if expected == 9:
                    if item != 0:
                        wrongPieces = wrongPieces + 1
                elif item != expected:
                    wrongPieces = wrongPieces + 1
                expected = expected + 1

        return wrongPieces

    # heuristica para calcular quantos passos de distancia cada peca esta
    def manhattanDistance(self):
        goal = [[1,2,3],[4,5,6],[7,8,9]]
        steps = 0
        for i in range(self.size):
            for j in range(self.size):
                pass

