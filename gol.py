# Game of Life: https://robertheaton.com/2018/07/20/project-2-game-of-life/
import random

def dead_board(width, height):
    board = [[0 for _ in range(0, width)] for _ in range(0, height)]
    return board

def rand_board(width, height):
    board = [[random.randint(0,1) for _ in range(0, width)] for _ in range(0, height)]
    return board

def count_neighbors(board, x, y):
    live_neighbors = 0
    has_left = 0
    has_right = 0
    has_above = 0
    has_below = 0

    if x > 0: has_above = 1
    if x < len(board)-1: has_below = 1
    if y > 0: has_left = 1
    if y < len(board[x])-1: has_right = 1

    # count 3 in row above
    if has_above:
        live_neighbors += board[x-1][y]
        if has_left: live_neighbors += board[x-1][y-1]
        if has_right: live_neighbors += board[x-1][y+1]

    # count 3 in row below
    if has_below:
        live_neighbors += board[x+1][y]
        if has_left: live_neighbors += board[x+1][y-1]
        if has_right: live_neighbors += board[x+1][y+1]

    # count 1 to left
    if has_left: live_neighbors += board[x][y-1]

    # count 1 to right
    if has_right: live_neighbors += board[x][y+1]

    return live_neighbors

def step_state(board):
    new_board = [[0 for _ in range(0, len(board))] for _ in range(0,len(board[0]))]
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            n = count_neighbors(board, x, y)
            if board[x][y]:
                if n <= 1 or n > 3: new_board[x][y] = 0
                else: new_board[x][y] = 1
            else:
                if n == 3: new_board[x][y] = 1
                else: new_board[x][y] = 0
    return new_board

def render_board(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print(chr(0x2591), end='', flush=True)
            else:
                print(chr(0x2588), end='', flush=True)
        print("")
