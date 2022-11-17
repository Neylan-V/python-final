import copy

from draws_boards import *
from update_board import *
#from get_move import *


START_BOARD_DIC = {'a1':4 , 'a2':4 , 'a3':4 , 'a4':4 , 'a5':4 , 'a6':4 , 'ap':0 , 'b1':4 , 'b2':4 , 'b3':4 , 'b4':4 , 'b5':4 , 'b6':4 , 'bp':0}

game_board_dict = copy.deepcopy(START_BOARD_DIC)


board_str = board(game_board_dict)
print(board_str)

player_move = 'a1'

update_board(game_board_dict, player_move)

#update_board()