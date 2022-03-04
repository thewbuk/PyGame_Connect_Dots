import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col-1] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col-1] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))

def win(board, piece):
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True

#Variables
ROW_COUNT = 6
COL_COUNT = 7
board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:
        while True:
            while True:
                try:
                    col = int(input('Player 1. Selection(0-6)'))
                except ValueError:
                    print('Choose only 1-6')
                    continue
                if col < 0 or col > 6:
                    print('Choose only 1-6')
                    continue
                else:
                    break
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                break
            else:
                continue
    

    if win(board,1):
        print('Player 1 win')
    else:
        while True:
            while True:
                try:
                    col = int(input('Player 2. Selection(0-6)'))
                except ValueError:
                    print('Choose only 1-6')
                    continue
                if col < 0 or col > 6:
                    print('Choose only 1-6')
                    continue
                else:
                    break

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                break
            else:
                print('here')
                continue
    
    if win(board,1):
        print('Player 1 win')
        
    print(print_board(board))
    

    turn += 1
    turn = turn % 2
