 ########## WHAT AM I DOING??????
# what functions?
# what main body?
# ...classes?
  # maybe the whole GAME is a class?
  # ok maybe not, based on the wheel of python reading, but the players could be classes?
    # maybe the board IS a class? what woud it do? would the updating of it go in a class or in the main program?
    # maybe update would be something like... board.update(current_board, start_pocket, num_tiles) 






##### MISC NOTES
# game end could be a checker that looks for one side of the board to be empty



### imports?

### classes
# define human_player class
# define computer_player class

### functions?
# check_winner: takes board (and player?) and checks to see if one side of     the board is empty, if one is, checks scores and returns TRUE, if not,      returns FALSE? or does that happen in a variable...
# draw_board: draws and returns initial board (should this be main program     stuff??)
# update_board: takes initial board and updates with new moves, returns new    board

### main
# welcomes players, describes rules? maybe gives options to describe rules     if needed
# draws board
# asks for num human players
  # creates instances of for those player(s)
  # if only one, creates instance for computer player
# roles dice to see which player goes first (first_player function?)
# asks for that players move
# updates board with that move
# checks for win
# updates score
# asks for next player's move
# checks for win
# updates score
# continues until one side of board is empty, at which point it checks for     a winner, declares the winner and updates player_winer to TRUE, which       causes end of while loop
  