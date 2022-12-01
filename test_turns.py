################# not a while loop #################
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



################# is a while loop #################
turns_taken = 10


while turns_taken > 0:
  print(board_str)

  if turns_taken%2 == 0: # THIS MUST GO used just to build test loops
    player = "player 1"
  else:
    player = "player 2"
    
  player_move = get_move(player)
  game_board_lst = update_board(game_board_lst, player_move)
  board_str = board(game_board_lst)

  turns_taken = turns_taken - 1
