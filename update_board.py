DEBUG = False

def update_board(board, move):
  tiles = board[move]
  next_pocket = move + 1
  while tiles > 0:
    
    tiles = tiles - 1
    board[next_pocket] = board[next_pocket] + 1
    next_pocket = (next_pocket + 1) % len(board)
  board[move] = 0
  
  return board



if DEBUG:
  print("hey it accessed update_board! crazy.")
  
  