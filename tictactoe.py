#set up Global variables
global winner

#check rows
row_winner = check_rows()
#check columns
column_winner = check_columns()
#check diagonals
diagonals_winner = check_diagonals
if row_winner:
winner = row_winner
elif column_winner:
winner = column_winner
elif diagonal_winner:
winner = diagonal_winner
else:
winner = None
return

def check_rows():
#set up global variables
global game_still_going
#check if any of the rows all have the same value ( and is not empty)
row_1 =board[0] == board[1] == board[2] ! = "-"
row_2 =board[3] == board[4] == board[5] ! = "-"
row_3 =board[6] == board[7] == board[8] ! = "-"
#if any of the rows does have
if row_1 or row_2 or row_3:
game_still_going = False
#return the winner ( X or O)

if row_1:
return board[O]
elif row_2:
return board[3]
elif row_3
return board[6]
return

def check_columns():
#set up global variables
global game_still_going
#check if any of the columns all have the same value ( and is not empty)
column_1 =board[0] == board[3] == board[6] ! = "-"
column_2 =board[1] == board[4] == board[7] ! = "-"
column_3 =board[2] == board[5] == board[8] ! = "-"
#if any of the rows does have
if column_1 or column_2 or column_3:
game_still_going = False
#return the winner ( X or O)
if column_1:
return board[O]
elif column_2:
return board[1]
elif column_3
return board[2]
return

def check_diagonals():
def check_diagonals():
#set up global variables
global game_still_going
#check if any of the diagonals all have the same value ( and is not empty)
diagonals_1 =board[0] == board[4] == board[8] ! = "-"
diagonals_2 =board[6] == board[4] == board[2] ! = "-"
#if any of the rows does have
if diagonals_1 or diagonal_2 or diagonal_3:
game_still_going = False
#return the winner ( X or O)
if diagonals_1:
return board[O]
elif diagonals_2:
return board[6]

return

def check_if_tie():
global game_still_going
if "-" not in board:
game_still_going = False
return
def flip_player():
#global variables we need
global current_player
#if current player was x then Change to o
if current_player == "X":
current_player = "O"
#if current player was o then change it x
elif current_player == "O":
current_player = "X"
return
play_game()