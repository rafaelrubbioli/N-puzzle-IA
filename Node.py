class Node:
    def __init__(self, board, empty, solution):
        self.board = board
        self.string = self.toString()
        self.empty = empty
        self.solution = solution
        self.last = None
        self.size = len(self.board)
        self.cost = -1
        self.n = self.size * self.size

    # troca as duas casas indicadas
    def switch(self, piece):
        self.board[self.empty] = self.board[piece]
        self.board[piece] = 0
        self.empty = piece
        self.string = self.toString()

    # transforma o tabuleiro em string para o explored
    def toString(self):
        boardString = ""
        for item in self.board:
            boardString = boardString + str(item)

        return boardString

    # imprime o tabuleiro na tela
    def show(self):
        print(self.string)

    # verifica se o jogo ja terminou
    def isOk(self):
        if self.toString() == "123456780":
            return True
        else:
            return False

    # busca quais sao as opcoes de movimento
    def possibleActions(self):
        empty = self.empty

        possibleActions = []
        # primeira casa da primeira coluna
        if empty == 0:
            possibleActions.append(1)
            possibleActions.append(3)

        # ultima da primeira linha
        elif empty == 1:
            possibleActions.append(0)
            possibleActions.append(2)
            possibleActions.append(4)

        # primeira casa da ultima linha
        elif empty == 2:
            possibleActions.append(1)
            possibleActions.append(5)

        # ultima casa da ultima linha
        elif empty == 3:
            possibleActions.append(0)
            possibleActions.append(4)
            possibleActions.append(6)

        # meio da primeira linha
        elif empty == 4:
            possibleActions.append(1)
            possibleActions.append(3)
            possibleActions.append(5)
            possibleActions.append(7)

        # meio da ultima linha
        elif empty == 5:
            possibleActions.append(2)
            possibleActions.append(4)
            possibleActions.append(8)

        # meio da lateral esquerda
        elif empty == 6:
            possibleActions.append(3)
            possibleActions.append(7)

        # meio da lateral direita
        elif empty == 7:
            possibleActions.append(6)
            possibleActions.append(4)
            possibleActions.append(8)

        # meio do tabuleiro
        else:
            possibleActions.append(7)
            possibleActions.append(5)

        return possibleActions

    # heuristica para calcular quantas casas estao erradas
    def numberOfWrongPieces(self):
        wrongPieces = 0
        for i, item in enumerate(self.string):
            if i == self.n - 1:
                if item != "0":
                    wrongPieces = wrongPieces + 1
            elif item != str(i+1):
                wrongPieces = wrongPieces + 1

        return wrongPieces

    # heuristica para calcular quantos passos de distancia cada peca esta
    def manhattanDistance(self):
        mandist = 0
        for i, item in enumerate(self.board):
            if item != 0:
                x1 = int(i / 3)
                y1 = i % 3
                x2 = int((item -1) / 3)
                y2 = (item -1) % 3
                mandist = mandist + abs(x1 - x2) + abs(y1 - y2)

        return mandist

    # mostra a solucao encontrada
    def showSolution(self):
        node = self
        while node.last:
            node.show()
            node = node.last
