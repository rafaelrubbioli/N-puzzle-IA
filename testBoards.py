# retorna uma tupla com o tabuleiro do numero escolhido
# e o local da casa vazia
def get(number):
    if number == 0:
        return [[1, 2, 3], [4, 5, 6], [7, 8, 0]], (2, 2)
    if number == 1:
        return [[1, 2, 3], [4, 5, 0], [7, 8, 6]], (1, 2)
    if number == 2:
        return [[1, 2, 3], [4, 0, 5], [7, 8, 6]], (1, 1)
    if number == 3:
        return [[1, 0, 3], [4, 2, 5], [7, 8, 6]], (0, 1)
    if number == 4:
        return [[1, 5, 2], [4, 0, 3], [7, 8, 6]], (1, 1)
    if number == 5:
        return [[1, 5, 2], [0, 4, 3], [7, 8, 6]], (1, 0)
    if number == 6:
        return [[1, 5, 2], [4, 8, 3], [7, 6, 0]], (2, 2)
    if number == 7:
        return [[1, 5, 2], [4, 8, 0], [7, 6, 3]], (1, 2)
    if number == 8:
        return [[0, 5, 2], [1, 8, 3], [4, 7, 6]], (0, 0)
    if number == 9:
        return [[1, 0, 2], [8, 5, 3], [4, 7, 6]], (0, 1)
    if number == 10:
        return [[5, 8, 2], [1, 0, 3], [4, 7, 6]], (1, 1)
    if number == 11:
        return [[5, 8, 2], [1, 7, 3], [4, 0, 6]], (2, 1)
    if number == 12:
        return [[], [], []], ()
    if number == 13:
        return [[], [], []], ()
    if number == 14:
        return [[], [], []], ()
    if number == 15:
        return [[8, 0, 2], [5, 7, 3], [1, 4, 6]], (0, 1)
    if number == 16:
        return [[], [], []], ()
    if number == 17:
        return [[], [], []], ()
    if number == 18:
        return [[], [], []], ()
    if number == 19:
        return [[], [], []], ()
    if number == 20:
        return [[], [], []], ()
    if number == 21:
        return [[], [], []], ()
    if number == 22:
        return [[], [], []], ()
    if number == 23:
        return [[], [], []], ()
    if number == 24:
        return [[], [], []], ()
    if number == 25:
        return [[], [], []], ()
    if number == 26:
        return [[], [], []], ()
    if number == 27:
        return [[], [], []], ()
    if number == 28:
        return [[], [], []], ()
    if number == 29:
        return [[], [], []], ()
    if number == 30:
        return [[], [], []], ()
    if number == 31:
        return [[8, 7, 6], [2, 5, 4], [3, 0, 1]], (2, 1)
