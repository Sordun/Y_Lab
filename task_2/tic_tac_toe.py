from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
За основу взят код https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py
но там 3х3
"""

HUMAN = -1
COMP = +1

board_size = 10  # РАЗМЕР ИГРОВОГО ПОЛЯ
number_for_win = 5  # СКОЛЬКО НУЖНО В РЯД ДЛЯ ПОБЕДЫ
comp_set_move = None  # Точка выбора компьютера

board = [[0] * board_size for item in range(board_size)]  # создание игрового поля


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """

    def win_list(num_list, number_for_win):
        """
        Функция для подсчёта всех столбцов, строк и по диагонали
        """
        return [
            num_list[num : num + number_for_win] for num in range(len(num_list) - 4)
        ]

    horizontally = []
    vertically = []
    diagonally_1 = []
    diagonally_2 = []
    count = 0
    count_2 = board_size - 1
    for w in range(board_size):
        tmp1 = []
        tmp2 = []
        for z in range(board_size):
            tmp1.append(state[w][z])
            tmp2.append(state[z][w])
        horizontally += win_list(tmp1, number_for_win)  # horizontally.append(tmp1)
        vertically += win_list(tmp2, number_for_win)  # vertically.append(tmp2)
        diagonally_1.append(tmp1[count])
        diagonally_2.append(tmp2[count_2])
        count += 1
        count_2 -= 1

    diagonally_1 = win_list(diagonally_1, number_for_win)
    diagonally_2 = win_list(diagonally_2, number_for_win)

    win_state = [*horizontally, *vertically, *diagonally_1, *diagonally_2]
    if [player] * number_for_win in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def valid_moves(board_size):
    moves = dict()
    count = 1
    for i in range(board_size):
        for x in range(board_size):
            moves[count] = [i, x]
            count += 1
    return moves


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(state, depth, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    :param c_choice: computer's choice +1
    :param h_choice: human's choice -1
    """

    chars = {-1: h_choice, +1: c_choice, 0: " "}
    str_line = "-------"

    print("\n" + str_line * board_size)
    cell_number = 1

    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f"|{cell_number:^3} {symbol} ", end="")
            cell_number += 1
        print(f"|", end="")
        print("\n" + str_line * board_size)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    global comp_set_move
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f"Computer turn [{c_choice}]")
    render(board, c_choice, h_choice)

    if depth > 9:
        x = choice(list(range(board_size)))  # выбираем случайную строку
        y = choice(list(range(board_size)))  # выбираем случайный столб
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    comp_set_move = (x * 10) + (y + 1)
    print(f"Компьютер выбрал: {comp_set_move}")
    time.sleep(1)
    return comp_set_move


def human_turn(c_choice, h_choice, comp_set_move):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :param comp_set_move: shows computer selection
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = valid_moves(board_size)

    clean()
    print(f"Human turn [{h_choice}]")
    render(board, c_choice, h_choice)
    print(f"Компьютер выбрал: {comp_set_move}")

    while move < 1 or move > board_size ** 2:
        try:
            move = int(input(f"Use numpad (1..{board_size**2}): "))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print("Bad move")
                move = -1
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ""  # X or O
    c_choice = ""  # X or O
    first = ""  # if human is the first

    # Human chooses X or O to play
    while h_choice != "O" and h_choice != "X":
        try:
            print("")
            h_choice = input("Choose X or O\nChosen: ").upper()
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")

    # Setting computer's choice
    if h_choice == "X":
        c_choice = "O"
    else:
        c_choice = "X"

    # Human may starts first
    clean()
    while first != "Y" and first != "N":
        try:
            first = input("First to start?[y/n]: ").upper()
        except (EOFError, KeyboardInterrupt):
            print("Bye")
            exit()
        except (KeyError, ValueError):
            print("Bad choice")

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == "N":
            ai_turn(c_choice, h_choice)
            first = ""

        human_turn(c_choice, h_choice, comp_set_move)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, COMP):
        clean()
        print(f"Human turn [{h_choice}]")
        render(board, c_choice, h_choice)
        print("COMP LOSE! YOU WIN!")
    elif wins(board, HUMAN):
        clean()
        print(f"Computer turn [{c_choice}]")
        render(board, c_choice, h_choice)
        print("YOU LOSE!")
    else:
        clean()
        render(board, c_choice, h_choice)
        print("DRAW!")

    exit()


if __name__ == "__main__":
    main()
