DEBUG = False
from draws_boards import *

def is_game_over(board):
  game_over = False
  if sum(board[0:6]) > 0:
    pass
  else:
    game_over = True
  if game_over == False:
    if sum(board[7:13]) > 0:
      pass
    else:
      game_over = True
  return game_over


def who_winner(board):
  p1 = sum(board[0:7])
  p2 = sum(board[7:])
  
  if is_game_over(board) == False:
    pass
  elif is_game_over(board) == True:
    if p1 == p1:
      player_winner = "tie" 
    elif p1 > p2:
      player_winner = "player 1"
    elif p1 < p2:
      player_winner = "player 2"
  
  return player_winner





############################ DEBUG ############################
if DEBUG:

  print("hey it accessed game_end DEBUG! crazy.")
  test_end_board = [0 , 0 , 0 , 0 , 0 , 0 , 3 , 1 , 1 , 1 , 1 , 1 , 1 , 2]
  final_score(test_end_board)
  
  print(board(test_end_board))
  
  
  print("this should return true: ", is_game_over(test_end_board))
  
  
  
  print("this should return player 1: " , who_winner(test_end_board))