
from draws_boards import *
from update_board import *
from get_move import *
from game_end import *

print(demo_board())

START_BOARD_LST = [4 , 4 , 4 , 4 , 4 , 4 , 0 , 4 , 4 , 4 ,  4 ,  4 ,  4 , 0]

game_board_lst = START_BOARD_LST[:]




player1 = "player 1" # have these be able to be names?
player2 = "player 2"
turns_taken = 0


while is_game_over(game_board_lst) == False:
  print(board(game_board_lst))

  if turns_taken%2 == 0: 
    player = "player 1"
  else:
    player = "player 2"

  player_move = get_move(player)
  game_board_lst = update_board(game_board_lst, player_move)
 
  turns_taken = turns_taken + 1


    
print(board(game_board_lst))
print("total turns taken: ", turns_taken)
print("the winner is: " , who_winner(game_board_lst))


