DEBUG = False

def board(board_lst): #make this use a for loop?
  str_lst = board_lst[:]
  for place in range(len(str_lst)):
    if str_lst[place] < 10:
      str_lst[place] = str(str_lst[place])
      str_lst[place] = str_lst[place] + ' '
  new_board= f'''   
         0    1    2    3    4    5
  -----------------------------------------
  |    | {str_lst[0]} | {str_lst[1]} | {str_lst[2]} | {str_lst[3]} | {str_lst[4]} | {str_lst[5]} |    |
  | {str_lst[13]}  -----------------------------  {str_lst[6]} | 
  |    | {str_lst[12]} | {str_lst[11]} | {str_lst[10]} | {str_lst[9]} | {str_lst[8]} | {str_lst[7]} |    |
  -----------------------------------------
         12   11   10    9    8    7
'''
  return(new_board)

def demo_board():
  board_lst = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,  10 ,  11 ,  12 , 13]
  str_lst = board_lst[:]
  for place in range(len(str_lst)):
    if str_lst[place] < 10:
      str_lst[place] = str(str_lst[place])
      str_lst[place] = str_lst[place] + ' '
  demo_board= f'''                   MANCALA  
                                   player 1
  -----------------------------------------
  |    | {str_lst[0]} | {str_lst[1]} | {str_lst[2]} | {str_lst[3]} | {str_lst[4]} | {str_lst[5]} |    |
  | {str_lst[13]}  -----------------------------  {str_lst[6]} | 
  |    | {str_lst[12]} | {str_lst[11]} | {str_lst[10]} | {str_lst[9]} | {str_lst[8]} | {str_lst[7]} |    |
  -----------------------------------------
  player 2
'''
  return  demo_board




if DEBUG:
  print("hey it accessed draw_board! crazy. \n below is what board with START_BOARD_DIC  should return")
  
  DEBUG_START_BOARD_LST = [4 , 4 , 4 , 4 , 4 , 4 , 0 , 4 , 4 , 4 ,4 ,4 , 4 , 0]
  
  print(board(DEBUG_START_BOARD_LST))

  print("and below this is what demo_board should return")
  
  print(demo_board())
