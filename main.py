import copy

from draws_boards import *
from update_board import *
from get_move import *

print(demo_board())

START_BOARD_LST = [4 , 4 , 4 , 4 , 4 , 4 , 0 , 4 , 4 , 4 ,  4 ,  4 ,  4 , 0]

game_board_lst = START_BOARD_LST[:]

board_str = board(game_board_lst)

print(board_str)

player1 = "player 1"

player_move = get_move(player1)

new_board = update_board(game_board_lst, player_move)

new_board_str = board(new_board)

print(new_board_str)

player2 = "player 2"

player_move = get_move(player2)

new_board = update_board(game_board_lst, player_move)

new_board_str = board(new_board)

print(new_board_str)
