DEBUG = False

# needs to take in an input, needs to make the move on the right side of the board, needs to return --the starting spot?--
def get_move(player):
  start_pocket = input(f"ok {player}, what pocket to start at? ")
  return int(start_pocket)
  







if DEBUG:
  print("hey it accessed get_move DEBUG! crazy.")
  player_1 = "Betty"
  player_1_move = get_move(player_1)
  print(player_1_move)