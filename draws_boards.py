DEBUG = False

def board(board_dic): #make this use a for loop?
  blank_board= (f'''                MANCALA!
  [    | {board_dic['a1']} | {board_dic['a2']} | {board_dic['a3']} | {board_dic['a4']} | {board_dic['a5']} | {board_dic['a6']} |    ]
  [ {board_dic['ap']} --------------------------- {board_dic['bp']} ]
  [    | {board_dic['b1']} | {board_dic['b2']} | {board_dic['b3']} | {board_dic['b4']} | {board_dic['b5']} | {board_dic['b6']} |    ]
  
  ''')
  return(blank_board)

def demo_board():
  board_dic = {'a1': 'a1' , 'a2':'a2' , 'a3':'a3' , 'a4':'a4' , 'a5':'a5' , 'a6':'a6' , 'ap':'ap' , 'b1':'b1' , 'b2':'b2' , 'b3':'b3' , 'b4':'b4' , 'b5':'b5' , 'b6':'b6' , 'bp':'bp'}
  demo_board= (f'''                MANCALA!
  [    | {board_dic['a1']} | {board_dic['a2']} | {board_dic['a3']} | {board_dic['a4']} | {board_dic['a5']} | {board_dic['a6']} |    ]
  [ {board_dic['ap']} ------------------------------- {board_dic['bp']} ]
  [    | {board_dic['b1']} | {board_dic['b2']} | {board_dic['b3']} | {board_dic['b4']} | {board_dic['b5']} | {board_dic['b6']} |    ] ''')
  return  demo_board




if DEBUG:
  print("hey it accessed draw_board! crazy. \n below is what board with START_BOARD_DIC  should return")
  
  DEBUG_START_BOARD_DIC = {'a1':4 , 'a2':4 , 'a3':4 , 'a4':4 , 'a5':4 , 'a6':4 , 'ap':0 , 'b1':4 , 'b2':4 , 'b3':4 , 'b4':4 , 'b5':4 , 'b6':4 , 'bp':0}
  
  print(board(DEBUG_START_BOARD_DIC))

  print("and below this is what demo_board should return")
  
  print(demo_board())
