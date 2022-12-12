DEBUG = False

# needs to take in an input, needs to make the move on the right side of the board, needs to return --the starting spot?--
def get_move(player, board):
  valid_move = False
  
  while valid_move == False:
    start_pocket = input(f"ok {player}, what pocket to start at? ")

    try:
      start_pocket = int(start_pocket)
      if start_pocket not in range(0,14):
        print("please enter a number corresponding to a pocket on your side of the board")
        valid_move = False
      elif start_pocket == 6 or start_pocket == 13:
        print("the manacalas are not acceptable start pockets! please try again.")
        valid_move = False
      elif player == "player 1" and start_pocket in (7,8,9,10,11,12):
        print("you must choose from your side of the board, not your opponent's")
        valid_move = False
      elif player == "player 2" and start_pocket in (0,1,2,3,4,5):
        print("you must choose from your side of the board, not your opponent's")
        valid_move = False
      elif board[start_pocket] == 0:
        print("your start pocket must have at least one tile in it, please pick another one!")
        valid_move == False
      else:
        valid_move = True
    except Exception:
      print("invalid input, please enter a number from 0 to 12")     
      valid_move == False
       
    
  return start_pocket
  







if DEBUG:
  print("hey it accessed get_move DEBUG! crazy.")
  player_1 = "Betty"
  player_1_move = get_move(player_1)
  print(player_1_move)