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
  if is_game_over(board) == False:
    pass
  elif is_game_over(board) == True:
    if board[6] == board[13]:
      player_winner = "tie" 
    elif board[6] > board[13]:
      player_winner = "player 1"
    elif board[6] < board[13]:
      player_winner = "player 2"
  
  return player_winner





############################ DEBUG ############################
if DEBUG:
  print("hey it accessed game_end DEBUG! crazy.")
  test_end_board = [0 , 0 , 0 , 0 , 0 , 0 , 3 , 1 , 1 , 1 , 1 , 1 , 1 , 2]
  print(board(test_end_board))
  
  
  print("this should return true: ", is_game_over(test_end_board))
  
  
  
  print("this should return player 1: " , who_winner(test_end_board))