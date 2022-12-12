
from draws_boards import *
from update_board import *
from get_move import *
from game_end import *

print(demo_board()) # displays which pockets are which


 ## GAME SET UP STUFF
START_BOARD_LST = [4 , 4 , 4 , 4 , 4 , 4 , 0 , 4 , 4 , 4 ,  4 ,  4 ,  4 , 0]

game_board_lst = START_BOARD_LST[:] # copy of OG list




player1 = "player 1" # have these be able to be names?
player2 = "player 2"
turns_taken = 0

print(board(game_board_lst)) # initial print of game board
## GAME SET UP OVER


## START MAIN GAME LOOP
while is_game_over(game_board_lst) == False: # loop for game play
  
  if turns_taken%2 == 0: 
    player = "player 1"
  else:
    player = "player 2"

  turn_over = False

  player_move = get_move(player, game_board_lst)
  end_pocket = player_move + game_board_lst[player_move]
  game_board_lst = update_board(game_board_lst, player_move)
  
  print(board(game_board_lst))

## START LOOP CHECKING FOR SPECIAL RULES
  while turn_over == False:
    if player == "player 1":
      if ( end_pocket in (0,1,2,3,4,5) ) and (game_board_lst[end_pocket] > 0):
        update_board(game_board_lst, end_pocket)
        end_pocket = player_move + game_board_lst[player_move]
        
        print(board(game_board_lst))
        
        if end_pocket == 6:
          print("You may pick another pocket!")
          player_move = get_move(player, game_board_lst)
          end_pocket = player_move + game_board_lst[player_move]
          game_board_lst = update_board(game_board_lst, player_move)
          
          print(board(game_board_lst))

  
      elif end_pocket == 6:
        print("You may pick another pocket!")
        player_move = get_move(player, game_board_lst)
        end_pocket = player_move + game_board_lst[player_move]
        game_board_lst = update_board(game_board_lst, player_move)
        
        print(board(game_board_lst))

  
      else:
        turn_over = True
      
    elif player == "player 2":
      
      if ( end_pocket in (7,8,9,10,11,12) ) and (game_board_lst[end_pocket] > 0):
        update_board(game_board_lst, end_pocket)
        end_pocket = player_move + game_board_lst[player_move]
        
        print(board(game_board_lst))

        if end_pocket == 13:
          print("You may pick another pocket!")
          player_move = get_move(player, game_board_lst)
          end_pocket = player_move + game_board_lst[player_move]
          game_board_lst = update_board(game_board_lst, player_move)
          
          print(board(game_board_lst))

  
      elif end_pocket == 13:
        print("You may pick another pocket!")
        player_move = get_move(player, game_board_lst)
        end_pocket = player_move + game_board_lst[player_move]
        game_board_lst = update_board(game_board_lst, player_move)
        
        print(board(game_board_lst))
  
      else:
        turn_over = True


  turns_taken = turns_taken + 1

## END MAIN GAME LOOP

# game play now over, final display of board, winner, and turns taken    
print(board(game_board_lst))
print("total turns taken: ", turns_taken)
print("the winner is: " , who_winner(game_board_lst))





