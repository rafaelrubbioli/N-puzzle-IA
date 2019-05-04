class Node:
    def __init__(self, board, empty, solution):
        self.board = board
        self.string = self.toString()
        self.empty = empty
        self.solution = solution
        self.last = None
        self.size = 3
        self.cost = -1
        self.n = 9
        self.depth = 0

    # troca as duas casas indicadas
    def switch(self, piece):
        self.board[self.empty] = self.board[piece]
        self.board[piece] = 0
        self.empty = piece
        self.string = self.toString()

    # transforma o tabuleiro em string para o explored
    def toString(self):
        boardString = str(self.board)

        return boardString

    # imprime o tabuleiro na tela
    def show(self):
        print(self.string)

    # verifica se o jogo ja terminou
    def isOk(self):
        if self.string == "[1, 2, 3, 4, 5, 6, 7, 8, 0]":
            return True
        else:
            return False

    # busca quais sao as opcoes de movimento
    def possibleActions(self):
        empty = self.empty

        if empty == 0:
            return 1, 3

        elif empty == 1:
            return 0, 2, 4

        elif empty == 2:
            return 1, 5

        elif empty == 3:
            return 0, 4, 6

        elif empty == 4:
            return 1, 3, 5, 7

        elif empty == 5:
            return 2, 4, 8

        elif empty == 6:
            return 3, 7

        elif empty == 7:
            return 6, 4, 8

        else:
            return 7, 5


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
